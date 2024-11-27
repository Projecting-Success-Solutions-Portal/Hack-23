# Challenge #1

**Schedule Summarisation**

**Summary**

Project planners often need to summarise schedules three reasons:
1) They need to integrate another stakeholder’s schedule into their own. This might be from a
supplier or another delivery partner.
2) They are asked to provide a summary of their plan to a project board or a senior
stakeholder where providing a detailed schedule would be inappropriate.
3) They can be a useful communication tool, enabling the whole plan to be discussed without
having to go into high levels of detail.
Two things are important when summarising a schedule - ensuring the summary accurately
reflects detailed schedules from a sequencing and timing perspective and accurately
reflects the progress or performance of the detailed schedule

**Pain Points​**

· I want to be able to visually summarise a detailed schedule in varying levels of detail. For
example, I want to summarise a 10,000-line schedule to 5000 lines, 1000 lines, 100 lines or 10
lines.
· I want to be able to be able to do the above visually but also be able to accurately represent
schedule progress/performance.
· I want to be able to update the summary schedule on an ongoing basis without the planner's
effort.


**Personas​**

As a Planner, I want to be able to automatically summarise supplier schedules into my plan,
while still being accurate in terms of sequencing and progress.
As a Planner, I want to be able to create summary plans from my schedule to satisfy senior
stakeholders that don’t need to see every line but still communicate the key elements of my
schedule.
As a senior leader, I want to only see a high-level summary of the schedule, So that I can
make a quick and informed decision on my requirements and interventions

**Business Context​**

Planners often need to summarise schedules. A summary schedule provides a high-level view of the
entire project or plan at a glance, allowing stakeholders to quickly grasp the big picture without
getting lost in detail. It's an effective tool for communicating key milestones, phases, and deadlines to
various stakeholders, including those who may not need or want all the intricate details.
Executives and managers often use summary schedules to make strategic decisions, as they can
easily see the overall timeline and major project components. Complex projects with numerous tasks
and dependencies can be overwhelming. A summary schedule simplifies the information, making it
more digestible. High-level views assist in broad resource allocation and planning across different
project phases.
A well-constructed summary schedule helps highlight the most crucial elements of a project, often
emphasising the critical path and key deliverables. They are useful for status reporting, especially to
upper management or clients who need to stay informed without diving into specifics.
Contextual understanding helps team members understand how their specific tasks fit into the larger
project context.

In meetings or presentations, a summary schedule allows for quicker discussions about overall
project progress and timing.

However, there are several risks when doing this:
· Not summarising accurately e.g., making errors.
· Not keeping the important details which then prove to be critical or crucial to the project.

This leads to the tasks taking a long time, as summary schedules are generally produced manually,
and this is made worse by it having to be repeated each time a summary schedule is needed.

**Dataset Description**​

A detailed schedule is provided as a .xer file and a .csv file. This schedule is publicly available.

**Success Criteria​**

For this challenge, we want teams to develop a schedule summary tool that can ingest a
detailed schedule and output a summary of that schedule at different levels while still
capturing schedule progress.
· It needs to be able to run on an as-needed basis, with different filters for different levels of
detail depending on different audiences.
· It needs to show the project's timeline clearly and text needs to be simple and readable.
· It needs to be able to reflect schedule progress/performance accurately.
· Visuals need to be used to aid understanding, with consistent conditional formatting
denoting different types of activity with a clear legend.
· It needs to show the important dependencies to aid understanding of the schedule flow.
· It needs to ensure it captures the key aspects of reporting against a schedule e.g., critical
paths, schedule milestones
· It needs to be based on some set rules which are clear to the user/planner.
Additionally, it would be great if the solution provided a summary narrative, integrated
directly with .xer files, and showed how the summary has changed over the last interval

**Benefits​**

If summarising the schedules can be automated, it should:
· Allow the planner to spend more time on planning rather than summarising schedules.
· It should allow the planner to focus on the key activities that are driving their project as the
driving activities that should be represented in the summary schedule.
· Provide a useful visual communication aid for planners to provide to stakeholders.
