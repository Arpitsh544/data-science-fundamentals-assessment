const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow,
  TableCell, WidthType, ShadingType, BorderStyle, AlignmentType,
  LevelFormat, convertInchesToTwip,
} = require("docx");

const H = (text, level) => new Paragraph({ text, heading: level, spacing: { before: 240, after: 120 } });
const P = (text, opts = {}) => new Paragraph({ children: [new TextRun(text)], spacing: { after: 160 }, ...opts });
const Bullet = (text) => new Paragraph({
  text, numbering: { reference: "bullets", level: 0 }, spacing: { after: 80 },
});

function cell(text, opts = {}) {
  return new TableCell({
    width: { size: opts.width || 2000, type: WidthType.DXA },
    shading: opts.header ? { fill: "2F5496", type: ShadingType.CLEAR } : undefined,
    children: [new Paragraph({
      children: [new TextRun({ text, bold: !!opts.header, color: opts.header ? "FFFFFF" : undefined })],
    })],
  });
}

const colWidths = [2200, 2200, 4600];

const typeTable = new Table({
  columnWidths: colWidths,
  width: { size: 9000, type: WidthType.DXA },
  rows: [
    new TableRow({ children: [cell("Column", { header: true, width: colWidths[0] }), cell("Data Type", { header: true, width: colWidths[1] }), cell("Handling Notes", { header: true, width: colWidths[2] })] }),
    new TableRow({ children: [cell("student_id", { width: colWidths[0] }), cell("Numerical (discrete)", { width: colWidths[1] }), cell("Unique identifier; not used in statistics", { width: colWidths[2] })] }),
    new TableRow({ children: [cell("age", { width: colWidths[0] }), cell("Numerical (discrete)", { width: colWidths[1] }), cell("Summary statistics, ranges", { width: colWidths[2] })] }),
    new TableRow({ children: [cell("grade", { width: colWidths[0] }), cell("Ordinal", { width: colWidths[1] }), cell("Preserve rank order (A > B > C > D)", { width: colWidths[2] })] }),
    new TableRow({ children: [cell("city", { width: colWidths[0] }), cell("Categorical (nominal)", { width: colWidths[1] }), cell("Frequency counts, encoding", { width: colWidths[2] })] }),
    new TableRow({ children: [cell("enrollment_date", { width: colWidths[0] }), cell("Datetime", { width: colWidths[1] }), cell("Parse to datetime, extract year/month", { width: colWidths[2] })] }),
    new TableRow({ children: [cell("score", { width: colWidths[0] }), cell("Numerical (continuous)", { width: colWidths[1] }), cell("Mean, median, variance, correlation", { width: colWidths[2] })] }),
    new TableRow({ children: [cell("remarks", { width: colWidths[0] }), cell("Text", { width: colWidths[1] }), cell("Cleaning, word/character counts", { width: colWidths[2] })] }),
  ],
});

const statsColWidths = [3500, 2500];
const statsTable = new Table({
  columnWidths: statsColWidths,
  width: { size: 6000, type: WidthType.DXA },
  rows: [
    new TableRow({ children: [cell("Statistic", { header: true, width: statsColWidths[0] }), cell("Value", { header: true, width: statsColWidths[1] })] }),
    new TableRow({ children: [cell("Mean", { width: statsColWidths[0] }), cell("75.86", { width: statsColWidths[1] })] }),
    new TableRow({ children: [cell("Median", { width: statsColWidths[0] }), cell("77.90", { width: statsColWidths[1] })] }),
    new TableRow({ children: [cell("Mode", { width: statsColWidths[0] }), cell("45.20", { width: statsColWidths[1] })] }),
    new TableRow({ children: [cell("Variance (sample)", { width: statsColWidths[0] }), cell("237.86", { width: statsColWidths[1] })] }),
    new TableRow({ children: [cell("Std. Deviation", { width: statsColWidths[0] }), cell("15.42", { width: statsColWidths[1] })] }),
    new TableRow({ children: [cell("25th percentile", { width: statsColWidths[0] }), cell("64.85", { width: statsColWidths[1] })] }),
    new TableRow({ children: [cell("75th percentile", { width: statsColWidths[0] }), cell("88.28", { width: statsColWidths[1] })] }),
  ],
});

const doc = new Document({
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT }],
    }],
  },
  sections: [{
    properties: {
      page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } },
    },
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 80 },
        children: [new TextRun({ text: "Data Science Fundamentals Assessment", bold: true, size: 32 })],
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 300 },
        children: [new TextRun({ text: "Task 1 Submission Report — Data Science Internship Program", italics: true, size: 22, color: "555555" })],
      }),

      H("1. Overview", HeadingLevel.HEADING_1),
      P("This report accompanies the notebook Data_Science_Fundamentals_Assessment.ipynb, submitted for Task 1 of the Data Science internship program. The notebook and this report together demonstrate understanding of the Data Science lifecycle, core Python programming, statistical foundations, data types and structures, and clean coding practices, closing with a set of practical programming assignments."),

      H("2. Data Science Lifecycle", HeadingLevel.HEADING_1),
      P("A typical Data Science project was studied as six stages, applied conceptually in this task:"),
      Bullet("Problem Definition — clarifying the business question and success criteria"),
      Bullet("Data Collection — gathering data from files, databases, or APIs"),
      Bullet("Data Cleaning & Preparation — handling missing values, duplicates, and type issues"),
      Bullet("Exploratory Data Analysis — summarizing and visualizing to find patterns"),
      Bullet("Modeling / Analysis — applying statistics or machine learning"),
      Bullet("Communication — presenting findings through reports and visualizations"),
      P("The four common categories of analysis (descriptive, diagnostic, predictive, and prescriptive) and representative industry use cases such as fraud detection, recommendation engines, and demand forecasting were also reviewed as part of this task."),

      H("3. Python Programming Basics", HeadingLevel.HEADING_1),
      P("The notebook implements and demonstrates the following Python fundamentals, each with runnable examples:"),
      Bullet("Variables and core data types: str, int, float, bool"),
      Bullet("Arithmetic, comparison, and logical operators"),
      Bullet("Conditional statements (if / elif / else) via a grade-banding function"),
      Bullet("for and while loops"),
      Bullet("Functions with docstrings, e.g. descriptive_summary()"),
      Bullet("Lists, tuples, dictionaries, and sets, with their mutability and ordering properties"),
      Bullet("Basic file handling — writing to and reading from a text file"),

      H("4. Statistical Foundations", HeadingLevel.HEADING_1),
      P("Descriptive statistics were computed on a sample of ten scores using NumPy and SciPy:"),
      statsTable,
      new Paragraph({ text: "", spacing: { after: 200 } }),
      P("Probability was illustrated with a simple empirical calculation — the proportion of sampled scores at or above 80 — and correlation was demonstrated between simulated study hours and exam scores using pandas' .corr() method, with an explicit note that correlation does not imply causation."),

      H("5. Data Types & Structures", HeadingLevel.HEADING_1),
      P("A small sample dataset (data/students_sample.csv, 15 records) was used to classify each column into numerical, categorical, ordinal, datetime, or text types, and to note how each should be handled during analysis:"),
      typeTable,
      new Paragraph({ text: "", spacing: { after: 200 } }),

      H("6. Best Practices Applied", HeadingLevel.HEADING_1),
      Bullet("Meaningful variable and function names throughout the notebook"),
      Bullet("Docstrings and markdown commentary explaining intent before implementation"),
      Bullet("A version-controlled, self-contained repository (sample data ships with the code) for reproducibility"),
      Bullet("Cautious, non-causal interpretation of statistical results"),

      H("7. Practical Assignments Completed", HeadingLevel.HEADING_1),
      Bullet("Sum, average, and product of four integers"),
      Bullet("Average of a list of numbers"),
      Bullet("Swapping the values of two variables"),
      Bullet("Printing numbers 1–10 using while and for loops"),
      Bullet("Extracting digits in odd positions of a 5-digit number"),
      Bullet("Binary search over a sorted list"),
      Bullet("String concatenation and length calculation"),
      Bullet("Smallest of three numbers"),
      Bullet("Word, character, whitespace, and special-symbol counts in a text string"),

      H("8. Conclusion", HeadingLevel.HEADING_1),
      P("All six objectives of the Fundamentals Assessment — the Data Science lifecycle, Python programming basics, statistical foundations, data types and structures, best practices, and the practical assignments — were completed and are demonstrated with runnable, documented code in the accompanying notebook and GitHub repository."),

      H("9. Repository", HeadingLevel.HEADING_1),
      P("GitHub repository: <insert your repository URL here after pushing>"),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  require("fs").writeFileSync("report.docx", buf);
  console.log("report.docx written");
});
