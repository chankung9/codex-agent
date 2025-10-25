use std::error::Error;
use std::fs;
use std::path::{Path, PathBuf};

use chrono::{Datelike, Utc};
use clap::Parser;

const AUTOMATION_HEADING: &str = "## Automation Notes";

#[derive(Parser, Debug)]
#[command(about = "Rust implementation of the Codex agent router.")]
struct Cli {
    /// Agent command string, e.g., "@finance summary"
    command: String,

    /// Optional content appended to the target artifact
    #[arg(short = 'c', long = "content", default_value = "")]
    content: String,

    /// Override repository root (defaults to current working directory)
    #[arg(long = "root")]
    root_override: Option<PathBuf>,
}

fn main() {
    if let Err(err) = run() {
        eprintln!("Error: {err}");
        std::process::exit(1);
    }
}

fn run() -> Result<(), Box<dyn Error>> {
    let cli = Cli::parse();

    let root = cli
        .root_override
        .map(fs::canonicalize)
        .transpose()?
        .unwrap_or_else(|| std::env::current_dir().expect("current dir available"));

    match cli.command.trim() {
        "@finance summary" => handle_finance_summary(&root, cli.content.trim())?,
        "@compliance audit" => handle_compliance_audit(&root, cli.content.trim())?,
        other => {
            let available = ["@finance summary", "@compliance audit"].join(", ");
            return Err(
                format!("Unknown command '{other}'. Available commands: {available}").into(),
            );
        }
    }

    Ok(())
}

fn timestamp() -> String {
    Utc::now().format("%Y-%m-%d %H:%M UTC").to_string()
}

fn ensure_finance_file(root: &Path, month: &str) -> Result<PathBuf, Box<dyn Error>> {
    let finance_dir = root.join("finance");
    let target = finance_dir.join(format!("summary_{month}.md"));
    if target.exists() {
        return Ok(target);
    }

    fs::create_dir_all(&finance_dir)?;
    let template_path = finance_dir.join("summary_TEMPLATE.md");
    let template = fs::read_to_string(&template_path).unwrap_or_default();
    let month_label = chrono::NaiveDate::parse_from_str(&format!("{month}-01"), "%Y-%m-%d")
        .map(|d| d.format("%B %Y").to_string())
        .unwrap_or_else(|_| month.to_string());

    let default_body =
        format!("# Monthly Finance Summary — {month_label}\n\n- Draft created automatically.\n");

    let filled = if template.is_empty() {
        default_body
    } else {
        template
            .replace("<Month YYYY>", &month_label)
            .replace("<YYYY-MM>", month)
    };

    fs::write(&target, filled.trim_end().to_string() + "\n")?;
    Ok(target)
}

fn append_automation_note(path: &Path, line: &str) -> Result<(), Box<dyn Error>> {
    let mut contents = fs::read_to_string(path)?;
    while contents.ends_with('\n') {
        contents.pop();
    }

    if !contents.contains(AUTOMATION_HEADING) {
        contents.push_str(&format!("\n\n{AUTOMATION_HEADING}\n"));
    } else if !contents.ends_with('\n') {
        contents.push('\n');
    }

    contents.push_str(&format!("- {line}\n"));
    fs::write(path, contents)?;
    Ok(())
}

fn handle_finance_summary(root: &Path, note: &str) -> Result<(), Box<dyn Error>> {
    let today = Utc::now().date_naive();
    let month = format!("{:04}-{:02}", today.year(), today.month());
    let path = ensure_finance_file(root, &month)?;
    let entry = if note.is_empty() {
        "No additional context provided."
    } else {
        note
    };
    append_automation_note(&path, &format!("{} — {}", timestamp(), entry))?;

    let display = path.strip_prefix(root).unwrap_or(&path);
    println!("Logged finance summary note in {}", display.display());
    Ok(())
}

fn ensure_audit_file(root: &Path, day: &str) -> Result<PathBuf, Box<dyn Error>> {
    let audit_dir = root.join("audit").join("logs");
    let path = audit_dir.join(format!("{day}.md"));
    if path.exists() {
        return Ok(path);
    }

    fs::create_dir_all(&audit_dir)?;
    fs::write(&path, format!("# Audit Log — {day}\n"))?;
    Ok(path)
}

fn handle_compliance_audit(root: &Path, note: &str) -> Result<(), Box<dyn Error>> {
    let today = Utc::now().date_naive();
    let day = format!(
        "{:04}-{:02}-{:02}",
        today.year(),
        today.month(),
        today.day()
    );
    let path = ensure_audit_file(root, &day)?;
    let entry = if note.is_empty() {
        "No additional context provided."
    } else {
        note
    };

    let mut file = fs::OpenOptions::new().append(true).open(&path)?;
    use std::io::Write;
    writeln!(
        file,
        "- Event: {entry}\n  - Owner: Compliance Agent\n  - Timestamp: {}",
        timestamp()
    )?;

    let display = path.strip_prefix(root).unwrap_or(&path);
    println!("Logged compliance audit event in {}", display.display());
    Ok(())
}
