## Use tokens in email notifications

To input tokens in a alert email notification is possible to use to: Search metadata tokens, Result tokens, Job information tokens, Server tokens, Dashboard metadata tokens.

**Search metadata tokens**
- Email server hostname: `$action.email.hostname$`
- Search priority: `$action.email.priority$`
- Alert expiration time: `$alert.expires$`
- Alert severity level: `$alert.severity$`
- App context for the search: `$app$`
- Search cron schedule: `$cron_schedule$`
- Human-readable search description: `$description$`
- Search name: `$name$`
- The next time the search runs: `$next_scheduled_time$`
- Search owner: `$owner$`
- (Alert actions and scheduled reports only) Link to search results: `$results_link$`
- Search string: $search$
- (Alert actions only) Date when alert triggered, formatted as Month(string) Day, Year: $trigger_date$
- (Alert actions only) Time when alert triggered, formatted as epoch time: $trigger_time$
- Indicates if the search is from an alert, report, view, or the search command: $type$
- Link to view saved search: $view_link$

**Result tokens**
First value for the specified field name from the first search result row. Verify that the search generates the field being accessed: $result.fieldname$ 

**Dashboard metadata tokens**
- Dashboard label: $dashboard.label$
- Equivalent to $dashboard.label$: $dashboard.title$
- Dashboard description: $dashboard.description$
- Dashboard ID : $dashboard.id$

Source: https://docs.splunk.com/Documentation/Splunk/8.0.2/Alert/EmailNotificationTokens
