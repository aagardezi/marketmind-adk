import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools import agent_tool
from google.adk.tools import google_search
from .tools.generaltools import get_current_date
from .tools.finhubtools import symbol_lookup, company_news, company_profile, company_basic_financials, insider_sentiment, financials_reported, sec_filings

# def get_weather(city: str, time: str) -> dict:
#     """Retrieves the current weather report for a specified city.

#     Args:
#         city (str): The name of the city for which to retrieve the weather report.
#         time (str): The time for which to retrieve the weather report.


#     Returns:
#         dict: status and result or error msg.
#     """
#     if city.lower() == "new york":
#         return {
#             "status": "success",
#             "report": (
#                 "The weather in New York is sunny with a temperature of 25 degrees"
#                 " Celsius (77 degrees Fahrenheit). The time in  New York is "
#                 f"{time}"
#             ),
#         }
#     else:
#         return {
#             "status": "error",
#             "error_message": f"Weather information for '{city}' is not available.",
#         }


# def get_current_time(city: str) -> dict:
#     """Returns the current time in a specified city.

#     Args:
#         city (str): The name of the city for which to retrieve the current time.

#     Returns:
#         dict: status and result or error msg.
#     """

#     if city.lower() == "new york":
#         tz_identifier = "America/New_York"
#     else:
#         return {
#             "status": "error",
#             "error_message": (
#                 f"Sorry, I don't have timezone information for {city}."
#             ),
#         }

#     tz = ZoneInfo(tz_identifier)
#     now = datetime.datetime.now(tz)
#     report = (
#         f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
#     )
#     return {"status": "success", "report": report}

search_agent = Agent(
    name="search_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to search about anything"
    ),
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
    tools=[google_search],
)

symbol_lookup_agent = Agent(
    name="symbol_lookup_agent",
    model="gemini-2.5-flash",
    description=(
        "You are an agent helping an investment analyst get a stock symbol name from a company name"
    ),
    instruction=(
        "You are a symbol lookup agent. Use the symbol_lookup tool to get a symbol from a company name"
        "use the symbol_lookup tool to get a stock symbol from a company name"
        "the symbol will be needed for subsiquent sub agents"
    ),
    tools=[symbol_lookup]
)

company_news_agent = Agent(
    name="company_news_agent",
    model="gemini-2.5-flash",
    description=(
        "You are an agent helping an investment analyst get news for a stock symbol"
    ),
    instruction=(
        "You News analysis agent. Use the company sumbol to retrieve company news and create a detailed summary of the news"
        "use the company_news tool to get the company news for the company"
        "The news can be used as part of analysing investment stratagies"
    ),
    tools=[company_news]
)

company_profile_agent = Agent(
    name="company_profile_agent",
    model="gemini-2.5-flash",
    description=(
        "You are an agent helping an investment analyst a company profile for a stock symbol"
    ),
    instruction=(
        "Use the company symbol to retrieve company profile and create a detailed summary of the profile"
        "use the company_profile tool to get the company profile for the company"
        "The profile can be used as part of analysing investment stratagies"
    ),
    tools=[company_profile]
)

company_basic_financials_agent = Agent(
    name="company_basic_financials_agent",
    model="gemini-2.5-flash",
    description=(
        "You are an agent helping an investment analyst a get the company basic financials for a stock symbol"
    ),
    instruction=(
        "Use the company symbol to retrieve company basic financials and create a detailed summary of the financial statement of the company"
        "use the company_basic_financials tool to get the company basic financials for the company"
        "The financials can be used as part of analysing investment stratagies"
    ),
    tools=[company_basic_financials]
)

financials_reported_agent = Agent(
    name="financials_reported_agent",
    model="gemini-2.5-flash",
    description=(
        "You are an agent helping an investment analyst a analysing financials reported for a stock symbol"
    ),
    instruction=(
        "Use the company symbol to retrieve the financials reported for the company create a detailed summary of the financial statement of the company"
        "use the financials_reported tool to get the financials reported for the company"
        "The financials can be used as part of analysing investment stratagies"
    ),
    tools=[financials_reported]
)

sec_filings_agent = Agent(
    name="sec_filings_agent",
    model="gemini-2.5-flash",
    description=(
        "You are an agent helping an investment analyst a analysing sec filings for a company based on its stock symbol"
    ),
    instruction=(
        "Use the company symbol to retrieve the sec filings for the company and create a detailed summary of the filings"
        "use the sec_filings tool to get the sec filings for the company"
        "The filings can be used as part of analysing investment stratagies"
    ),
    tools=[sec_filings]
)

insider_sentiment_agent = Agent(
    name="insider_sentiment_agent",
    model="gemini-2.5-flash",
    description=(
        "You are an agent helping an investment analyst a analysing insider sentiment for a company based on its stock symbol"
    ),
    instruction=(
        "Use the company symbol to retrieve the insider sentiment for the company and create a detailed summary of it"
        "use the insider_sentiment tool to get the insider sentiment for the company"
        "The insider sentiment can be used as part of analysing investment stratagies"
    ),
    tools=[insider_sentiment]
)


root_agent = Agent(
    name="investment_agent",
    model="gemini-2.5-flash",
    description=(
        "You are an agent helping an investment analyst at an asset manager"
    ),
    instruction=(
        # "You are an investment analyst agent that creates an analysis of assets and stock"
        # "You use the tools and subagents at your disposal to get the data and summarise the data"
        # "Include a detailed summary in the response"
        # "use the get_current_date tool to get the current data in order to use with any of the subagents"
        # "use the symbol_lookup_agent to get a stock symbol from a company name"
        # "use the news subagent to get company news"
        # "In the response include a detailed section on the news"
        # "If the user does not specify a start date or end date, use the current date as the start date using the get_current_date tool"
        # "use the date from 6 months ago as the end date"
        # "If the user specifies the date as a duration, use get_current_date to get the start date and calculate it"
        # "make sure to always use the get_current_date tool to do the date calculation"
        # "use all the sub agnets to create a report on the investment"
        """You are a highly skilled financial analyst specializing in asset management. Your task is to conduct thorough financial analysis and generate detailed reports from an investor's perspective. Follow these guidelines meticulously:

                        **1. Symbol Identification and Lookup:**

                        *   **Primary Symbol Focus:** When multiple symbols exist for a company, prioritize the *primary* symbol, which typically does *not* contain a dot (".") in its name (e.g., "AAPL" instead of "AAPL.MX").
                        *   **Mandatory Symbol Lookup:** Before executing any other functions, always use the `symbol_lookup` function to identify and confirm the correct primary symbol for the company under analysis. Do not proceed without a successful lookup.
                        *   **Handle Lookup Failures:** If `symbol_lookup` fails to identify a symbol, inform the user and gracefully end the analysis.

                        **2. Date Handling:**

                        *   **Current Date Determination:** Use the `current_date` function to obtain the current date at the beginning of each analysis. This date is critical for subsequent time-sensitive operations.
                        *   **Default Year Range:** If a function call requires a date range and the user has not supplied one, calculate the start and end dates for the *current year* using the date obtained from `current_date`. Use these as the default start and end dates in the relevant function calls.

                        **3. Analysis Components:**

                        *   **Comprehensive Report:** Your report should be comprehensive, detailed and contain the following sections:
                            *   **Company Profile:**  Include a detailed overview of the company, its industry, and its business model.
                            *   **Company News:** Summarize the latest significant news impacting the company. Make it detailed.
                            *   **Basic Financials:** Present key financial metrics and ratios for the company, covering recent periods (using current year as default period).
                            *   **Peer Analysis:** Identify and analyze the company's key competitors, comparing their financials and market performance (current year default).
                            *   **Insider Sentiment:**  Report on insider trading activity and overall sentiment expressed by company insiders.
                            *   **SEC Filings:**  Provide an overview of the company's recent SEC filings, highlighting any significant disclosures and a summary of the findings. Make it detailed.

                        **4. Data Handling and Error Management:**

                        *   **Data Completeness:** If a function requires date that is not present or unavailable, use the current year as the default period. Report missing data but don't let it stop you.
                        *   **Function Execution:** Execute functions carefully, ensuring you have the necessary data, especially dates and symbols, before invoking any function.
                        *   **Clear Output:** Present results in a clear and concise manner, suitable for an asset management investor.

                        **5. Analytical Perspective:**

                        *   **Asset Management Lens:** Conduct all analysis with an asset manager's perspective in mind. Evaluate the company as a potential investment, focusing on risk, return, and long-term prospects.

                        **Example Workflow (Implicit):**

                        1.  Get the current date using `current_date`.
                        2.  Use `symbol_lookup_agent` to identify the primary symbol for the company provided by the user.
                        3.  If no symbol is found, end the process and report back.
                        4.  Calculate the start and end date by using the result of the get_current_date tool.
                        5.  Call the relevant sub agents to retrieve the company_profile_agent, company_news_agent, company_basic_financials_agent, insider_sentiment_agent, financials_reported_agent, and sec_filings_agent, news, financials, insider sentiment, and SEC filings. Use the current year start and end date when required, or the date specified by the user.
                        6.  Assemble a detailed and insightful report that addresses each of the sections mentioned above.
                        """
                        "Make sure you run all the sub agents"

    ),
    tools=[get_current_date],
    sub_agents=[symbol_lookup_agent, company_news_agent,company_profile_agent, company_basic_financials_agent, insider_sentiment_agent, financials_reported_agent, sec_filings_agent ]
)