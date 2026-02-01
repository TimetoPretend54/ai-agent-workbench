---
name: internet-search-searxng
description: Search the internet using SearXNG metasearch engine and use results for planning or coding tasks. Activate when asked to search online, find current information, research topics, check the internet for data, browse web, look up information, find recent articles, google something, search the web, find latest information, get online results, find info on, search for info about, look up details about, check the web for, research about, get information about, or when you need current data for coding tasks. Use this skill for any web search request.
license: MIT
metadata:
  author: ai-agent-workbench
  version: "1.0"
---

# Internet Search with SearXNG

When asked to search online or check the internet for information, first check if a search query was provided.

IF NO SEARCH QUERY WAS PROVIDED:
1. ASK THE USER WHAT THEY WANT TO SEARCH FOR
2. WAIT FOR THEIR RESPONSE
3. THEN EXECUTE THE SEARCH

IF SEARCH QUERY IS PROVIDED:
1. EXECUTE THE SEARXNG SEARCH SCRIPT DIRECTLY WITHOUT ANALYSIS

## Execution Command

### Windows OS

Use this command to search (the script is available globally via the system symlink):

```
python "%USERPROFILE%/.kilocode/system/scripts/query_searxng.py "{your search query here}" {number_results}
```

Then report back the results. If you need more detailed information from specific sources that were truncated, you can retrieve full content using:

```
python "%USERPROFILE%/.kilocode/system/scripts/query_searxng.py --url "{URL_from_initial_results}"
```

Alternatively, you can use curl to fetch content from specific URLs:

```
curl -s "{URL}"
```

### Mac / Linux OS

Use this command to search (the script is available globally via the system symlink):

```
python "~/.kilocode/system/scripts/query_searxng.py "{your search query here}" {number_results}
```

Then report back the results. If you need more detailed information from specific sources that were truncated, you can retrieve full content using:

```
python "~/.kilocode/system/scripts/query_searxng.py --url "{URL_from_initial_results}"
```

Alternatively, you can use curl to fetch content from specific URLs:

```
curl -s "{URL}"
```

## System Availability

This skill uses the globally available system scripts that are linked from $HOME/.kilocode/system/. The scripts are automatically managed by the system setup and are available from any project context.

## Avoid These Actions
- Do not explain the script
- Do not read the script
- Do not document implementation
- Do not check if SearXNG instance is running by checking the start script and the docker configuration
- Do not check the docker configuration for SearXNG to understand how it's set up
- Do not check the SearXNG settings file to understand the configuration
- Do not check if the SearXNG service is actually running by testing the endpoint
- Do not check if SearXNG service is running before executing searches

## Do These Actions
- Execute the script when asked for online information
- Use at least 10 results when specifying number of results
- Be in-depth with information analysis and evaluation, make sure to check all content's information, always double check
- Use the --url flag to get full content from specific sources when initial results are truncated and more detail is needed
- Note which sources have full content available for follow-up requests
- Analyze search results for relevance and quality before reporting
- Verify the accuracy of information from multiple sources when possible
- Consider the context and requirements of the current task when evaluating results
- If the primary ask tool fails with an error, report the error to the user and ask them to provide the search query directly in the next message

## Content Truncation Detection and Alternative Methods

### Primary Method: Script-based Fetching
Use the query_searxng.py script as the primary method for retrieving content from URLs.

### Alternative Method: Using Curl
As an alternative to the Python script, you can use curl to fetch content from specific URLs:

```
curl -s "{URL}"
```

This is particularly useful when:
- You need a quick fetch without Python overhead
- The Python script encounters issues
- You want to bypass certain content extraction complexities
- Testing raw HTTP response content

### Automatic Truncation Detection
- After running the initial search, carefully examine all results for the truncation indicator: `[Content truncated - full article continues at: URL]`
- Pay attention to results marked as truncated in the "CONTENT TRUNCATION DETECTED" section that appears at the end of results

### Decision Framework for Fetching More Content
Use this decision tree to determine when to fetch additional content:

1. **CRITICAL INFORMATION NEEDED**: If the truncated content appears to contain essential information directly related to your task, fetch it immediately
2. **HIGH RELEVANCE**: If the content seems highly relevant to your query but is cut off, fetch the complete version
3. **AUTHORITY SOURCE**: If the truncated content is from an authoritative source (.edu, .gov, .org, major news sites), consider fetching for verification
4. **RECENT CONTENT**: If the truncated content is recent (less than 6 months old) and highly relevant, prioritize fetching
5. **CITATION QUALITY**: If you need to cite or reference specific details that are truncated, fetch the complete content
6. **CONTEXT REQUIREMENT**: If the task requires comprehensive understanding that truncated content cannot provide, fetch full content

### Content Quality Assessment
Before deciding to fetch more content, evaluate:
- **Relevance**: How directly related is the truncated content to your current task?
- **Authority**: Is the source credible and trustworthy?
- **Recency**: Is the information current and applicable to your needs?
- **Completeness**: Will the truncated information be sufficient, or do you need the full details?
- **Accuracy**: Does the information align with other sources and known facts?
- **Context**: Does the content provide sufficient background for the current task?

### Selective Fetching Strategy
- **DO**: Fetch content from sources that show clear truncation markers when you need the complete information
- **DO**: Prioritize fetching from authoritative or highly relevant sources first
- **DO**: Fetch content when you need to verify critical information or get complete details
- **DON'T**: Fetch all truncated content automatically - be selective based on your actual needs
- **DON'T**: Fetch content that appears to be low-quality, outdated, or irrelevant to your task
- **DON'T**: Overload with too many sources when a few authoritative ones would suffice

### Post-Fetch Analysis
After fetching additional content:
- Compare the complete content with your original requirements
- Verify that the additional information is useful and relevant
- Assess whether the source is authoritative and trustworthy
- Determine if you need to fetch content from additional sources based on cross-references
- Synthesize information from multiple sources when appropriate
- Evaluate how the new information impacts your current task

### Performance Optimization
- Consider the time cost (1-3 seconds per URL) when deciding to fetch multiple sources
- Prioritize the most important sources first
- Use your judgment about whether the additional information is worth the time investment
- Adjust the number of initial results based on the complexity of the query (use fewer for simple fact-checking, more for complex research)
- Be mindful of context window limitations when processing large amounts of content

## Additional Context for New Agents

### Error Handling
- Be aware of potential timeout errors when fetching content from external URLs
- Some websites may block automated requests, resulting in empty content
- The script handles errors gracefully but may return limited information in these cases
- If a query returns no results, try rephrasing with alternative terms
- If multiple URLs fail, consider the possibility of network issues or blocked access

### Performance Considerations
- Fetching content from multiple URLs takes time (1-3 seconds per URL)
- The script processes results sequentially, so large numbers of results will take longer
- Using more than 15-20 results might lead to very long processing times
- For complex research tasks, consider starting with fewer results and expanding if needed
- Balance depth of research with efficiency based on the urgency of the request

### Content Freshness
- The script provides publication dates when available
- Older content might be less relevant for current queries
- AI systems often prefer recent information for certain types of queries
- When research requires current information, prioritize recent sources
- Note the publication date when reporting information that might be time-sensitive

### Authority Indicators
- Results from .edu, .gov, and well-known authoritative domains (.org, major news sites) may be weighted more heavily
- The script identifies and highlights these sources in the results
- When multiple sources conflict, prioritize information from authoritative sources
- Be aware that even authoritative sources can have limitations or biases
- Cross-reference information across multiple authority types when possible

### Truncation Awareness
- When content shows "[Content truncated - full article continues at: URL]", that's a signal that the source has more detailed information available
- The --url flag can be used to retrieve complete content from these sources via the Python script
- Alternatively, you can use curl to fetch the content directly: `curl -s "{URL}"`
- Some content may appear complete but lack important context - use judgment about completeness
- Look for key information that might be missing in truncated versions

### Context Window Optimization
- The script is designed to work within LLM context windows by providing structured, relevant information
- For deeper analysis, specific URLs can be queried individually to get more comprehensive content
- Be mindful of how much information you're processing at once
- Consider summarizing large amounts of content to fit within context constraints
- Use iterative approaches when dealing with very large or complex topics

### Retry Logic
- If a query returns no results or very limited results, consider rephrasing the search query
- The script will indicate when results may not be comprehensive
- Try breaking complex queries into smaller, more specific sub-queries
- Use different terminology or synonyms if initial queries are unsuccessful

### Follow-up Strategy
- After initial search, analyze the results to determine if more detailed information is needed from specific sources
- Use the --url flag selectively rather than fetching full content from all sources unless specifically needed
- As an alternative to the --url flag, you can use curl to fetch content directly: `curl -s "{URL}"`
- Consider the next steps in your task when deciding which sources to explore further
- Plan your research approach based on the complexity and requirements of the task

### Limitations
- The script depends on the local SearXNG instance being available and responsive
- Content extraction may not work well for sites with heavy JavaScript or complex paywalls
- Some websites may have anti-bot measures that prevent content extraction
- The quality of results depends on the indexing and availability of information online
- Real-time information may not be available depending on the SearXNG configuration

### Verification
- Always verify critical information from multiple sources when possible
- The script provides citations and sources to enable verification
- Be cautious with information that seems too good (or bad) to be true
- Cross-check numerical data, dates, and factual claims when accuracy is important
- Consider the potential for outdated or incorrect information in search results

### Agentic Thinking Process
- **Analyze**: Before executing searches, consider what specific information is needed
- **Plan**: Determine the best search terms and number of results for the task
- **Execute**: Run the search command with appropriate parameters
- **Review**: Evaluate the quality and relevance of results
- **Iterate**: Refine search strategy based on initial results if needed