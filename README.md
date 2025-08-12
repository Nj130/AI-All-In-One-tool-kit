♨️AI-AllInOne-toolkit is an open-source, AI-powered vulnerability detection toolkit for scanning codebases, container images, and network traffic to automatically discover, prioritize, and explain security issues.

Why this project?

Modern security tooling needs to combine signature-based detection with behavioral and ML-based anomaly detection. AI-AllInOne-toolkit provides a practical, extensible pipeline that uses lightweight ML models and rule-based checks to surface high-confidence findings with human-readable explanations.

Key features

✅ Static analysis for common insecure patterns (SQL injection, insecure deserialization, hard-coded secrets).

✅ Dynamic / heuristic checks for runtime misconfigurations and suspicious network patterns.

✅ ML anomaly detection trained on labeled vulnerability examples and benign code/traffic to flag unusual behavior.

✅ Explainable reports: each finding includes a confidence score, concise explanation, and remediation suggestion.

✅ Multiple input types: source code, Docker images, PCAP network captures, and logs.

✅ CI/CD friendly: run as a GitHub Action, GitLab job, or in your pipeline.

✅ Exportable results: JSON, SARIF, and HTML report formats.

Quickstart (Linux / macOS)

Assumes Python 3.10+ and pip installed.

# clone
git clone https://github.com/Nj130/AI-AllInOne-Toolkit.git
cd AI-AllInOne-Toolkit

# create venv
python -m venv .venv
source .venv/bin/activate

# install
pip install -r requirements.txt

# run a scan on a sample repo
python -m aics scanner --target ../some-repo --output report.json


Supported scan modes

   -static — source code pattern + ML-based token analysis

   -dynamic — runtime heuristics on logs/PCAP

   -container — scan Docker images for vulnerable packages & misconfigurations

   -all — runs all enabled checks
   
