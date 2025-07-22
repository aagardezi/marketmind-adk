# MarketMind: AI-Powered Investment Analyst

This project is an AI-powered investment analyst that uses a system of autonomous agents to conduct financial research. It automatically gathers and synthesizes company data, including news, financials, and SEC filings, to generate comprehensive investment reports.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Why Google's Agents Development Kit (ADK)?](#why-googles-agents-development-kit-adk)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Configuration](#installation--configuration)
- [Deployment & Usage](#deployment--usage)
- [Potential Customers](#potential-customers)
- [Contributing](#contributing)

## Features
*   **Automated Data Gathering**: Fetches company profiles, latest news, basic financials, insider sentiment, and SEC filings.
*   **Intelligent Synthesis**: Uses a final-layer agent to synthesize all collected data into a coherent, structured investment report.
*   **Dynamic Symbol Lookup**: Automatically finds the correct stock ticker for a given company name.
*   **Modular & Extensible**: New data sources or analytical capabilities can be added by creating new agents.
*   **Parallel Processing**: Leverages parallel agent execution to speed up the data collection process significantly.

## Architecture
MarketMind is built using a multi-agent system, where each agent is a specialized worker responsible for a specific task. This architecture is orchestrated using Google's ADK.

1.  **`symbol_lookup_agent`**: The entry point. It takes a company name and finds the corresponding stock symbol.
2.  **`data_retrieval_agent` (`ParallelAgent`)**: Once the symbol is found, this agent triggers multiple sub-agents to run concurrently, each fetching a different piece of information:
    *   `company_news_agent`
    *   `company_profile_agent`
    *   `company_basic_financials_agent`
    *   `insider_sentiment_agent`
    *   `sec_filings_agent`
3.  **`report_creation_agent`**: After all data is collected, this agent receives the outputs from the parallel agents. It synthesizes the information into a single, comprehensive financial report.

This entire workflow is wrapped in a `SequentialAgent` (`sqeuential_agent`) to ensure the steps run in the correct order: Symbol Lookup -> Data Retrieval -> Report Creation.

## Why Google's Agents Development Kit (ADK)?
The choice of Google's ADK was pivotal for building a sophisticated and maintainable agent-based system.

*   **Powerful Orchestration**: ADK provides high-level abstractions like `SequentialAgent` and `ParallelAgent` that make it simple to design and implement complex agent workflows. Orchestrating a multi-step, parallel data-gathering process becomes declarative and easy to understand.
*   **Modularity and Reusability**: The framework encourages breaking down large problems into smaller, manageable tasks, each handled by a distinct agent. These agents (`company_news_agent`, `sec_filings_agent`, etc.) are self-contained and can be easily reused in other financial analysis applications.
*   **Seamless Tool Integration**: ADK simplifies the process of equipping agents with tools. The project seamlessly integrates custom tools (like the Finnhub API wrappers) and pre-built Google tools (`google_search`), allowing agents to interact with external data sources and services effectively.
*   **Scalability**: The modular, agent-based design is inherently scalable. To add a new data source (e.g., stock price history or social media sentiment), we only need to create a new tool and a corresponding agent and plug it into the `data_retrieval_agent` without refactoring the core logic.

## Getting Started

### Prerequisites
*   Python 3.9+
*   A Google Cloud Project with the Secret Manager API enabled.
*   Google Cloud SDK installed and authenticated.
*   A Finnhub API Key.

### Installation & Configuration

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd marketmind-adk
    ```

2.  **Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    The `requirements.txt` file has been updated with all necessary packages.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Authenticate with Google Cloud:**
    This allows the application to access GCP services like Secret Manager.
    ```bash
    gcloud auth application-default login
    ```

5.  **Store your Finnhub API Key in Secret Manager:**
    Replace `[YOUR_PROJECT_ID]` with your Google Cloud Project ID and `[YOUR_FINNHUB_API_KEY]` with your key. The application is hardcoded to look for a secret named `FinHubAccessKey`.
    ```bash
    gcloud secrets create FinHubAccessKey --replication-policy="automatic" --project="[YOUR_PROJECT_ID]"
    echo -n "[YOUR_FINNHUB_API_KEY]" | gcloud secrets versions add FinHubAccessKey --data-file=- --project="[YOUR_PROJECT_ID]"
    ```

## Deployment & Usage
This project is designed as a library of agents. You can import and run the main agent (`root_agent`) from your own Python scripts.

1.  **Create a `run.py` file in the root directory (a sample has been provided):**

    ```python
    # run.py
    import asyncio
    from investment_analyst_agent.agent import root_agent

    async def main():
        """
        Main function to run the investment analyst agent.
        """
        company_name = "NVIDIA"
        print(f"🚀 Starting analysis for: {company_name}")

        try:
            result = await root_agent.invoke(company_name)
            print("\n✅ Analysis Complete. Final Report:")
            print("------------------------------------")
            print(result)
            print("------------------------------------")
        except Exception as e:
            print(f"An error occurred during analysis: {e}")

    if __name__ == "__main__":
        asyncio.run(main())
    ```

2.  **Run the script:**
    From your terminal, simply execute the file:
    ```bash
    python run.py
    ```
    The agent will then begin the analysis process, printing the final, synthesized report to the console upon completion.

## Potential Customers
This automated financial research agent can provide significant value to a wide range of users in the financial industry:

*   **Asset Managers & Investment Analysts**: Automates the time-consuming process of data collection and preliminary analysis, allowing them to focus on high-level strategic decision-making and alpha generation.
*   **Hedge Funds**: Can be integrated into quantitative and qualitative analysis pipelines to quickly generate due diligence reports on potential investment targets, increasing the speed and breadth of market coverage.
*   **Retail Investors**: Empowers sophisticated individual investors with institutional-grade research tools, enabling them to make more informed decisions.
*   **Fintech Platforms**: Robo-advisors and financial content platforms can use this as a backend engine to provide automated, data-rich company analysis to their users.
*   **Financial Consultants & M&A Advisors**: Speeds up the initial due diligence phase when evaluating companies for mergers, acquisitions, or strategic partnerships.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs, feature requests, or improvements.