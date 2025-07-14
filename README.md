This is my solution to the GitHub User Activity CLI on roadmap.sh
https://roadmap.sh/projects/github-user-activity

It is a terminal-based Python script that fetches and displays recent activity for a GitHub user. It uses the GitHub REST API to show a breakdown of events like pushes, issue openings, and starred repositories in a clean, readable format.

---

## Features
  **GitHub User Input**: Accepts any public GitHub username.
  **Push Events**: Displays how many commits were pushed and to which repository.
  **Issue Events**: Shows opened issues with their titles.
  **Starred Repos**: Displays repos that the user has recently starred.
  **Live API Integration**: Fetches real-time data using the GitHub REST API.

---

## How to Run It
Make sure you have the required libraries installed:
  requests
  prettytable

## Future Improvements
  **Formatted Table View**: Use `PrettyTable` to neatly display output in tabular format.
  **Pagination Support**: View more than the default 30 events.
  **Date Filtering**: Allow filtering events by a specific date or range.
  **Event Type Selector**: Let users choose which event types to display.
  **Offline Logging**: Option to save the activity logs to a local file.
  **Unit Tests**: Add test cases to verify response handling and error conditions.
