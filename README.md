# jira-timekeeper
A simple timer and time entry repository app to make adding time in Jira automated and effortless.
Jira is pretty neat, but entering time spent on tasks can take a lot of time better spent being productive. No one likes administrivia, so this is meant to provide a better way.

## MVP Requirements
Here are the application requirements in relation to the existing Jira features.

### Time entry
There are really only three or four things required to add a time entry in Jira.
* Start timestamp
* End timestamp
* Issue ID
* Description (Optional in Jira)

Pretty simple, right?

### Desktop runtime environment
Jira's browser based timer allows a user to time their current task, but it's pretty inflexible and doesn't allow the user to easily
change things later if they forget to start or stop it (which I do often).
Due to the limitations of the timer running in the browser, the UX isn't great. I'd rather have an actual desktop window that both
reminds me where I'm at with the current task, and allows me to start another time entry easily.

### Timesheet review
I really want the ability to review the timesheet *before* submitting the time entries to Jira so I can make any corrections that may
be necessary. Once time entries are submitted, they are considered immutable.

### Jira REST service integration
All Jira interactions should happen over the [REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/) that exists with
most any Jira installation I've encountered, including the cloud version.

### Jira issue synchronization
The application should be able to get basic issue information and post time entries to it with the timesheet submission process.

### Validation and Error handling
There are a few things that could mess up this process.
* Since Jira is client/server based, the time entries that are already entered on the issue could change at any time. To handle this,
there should be a pre-flight check to determine whether the application's view of time entries matches the server's, since the user may
want to respond to this change.
* Connectivity, server, or access issues should be handled gracefully. If there are extended outages, then the application should be
able to locally store timesheets to be submitted later.
* Jira doesn't allow a user to input a time entry that starts before midnight and ends afterwards, but late hours spent on support
rotations or beating deadlines have shown that this happens. The application should be able to handle this situation by creating two
entries for the user.

## Post-MVP Features
If this ends up being something I use often, I may want to add more convenience features. I'll add issues to this repo as appropriate
to describe these additional features.
