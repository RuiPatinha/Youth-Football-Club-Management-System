Youth Football Club Management System
Project objective

A digital platform for managing a youth football club, connecting administrators, coaches/staff, players and parents in one system.

The system will have a central database, a web application accessible from computers and phones, and eventually could be extended into a dedicated mobile app.



Users

The system will have different types of users.

Administrator

Responsible for managing the club.

Can:

Create/edit/delete players
Create/edit/delete staff
Create/edit/delete teams
Create seasons
Assign players to teams
Assign staff to teams
Manage fields
Create matches
Manage training sessions
Manage convocations
Communicate with staff
Staff / Coach

Can:

View their teams
View players
View player information
Schedule/view training
Record player availability
Record attendance
View/create match information depending on permissions
Create weekly convocations
Communicate with parents
Communicate with administrators
Parent

Can:

View their children
View their child's team
See training sessions
Confirm whether their child will attend training
See matches
See convocations
Receive messages from coaches/staff
Communicate with coaches/staff


2. Player Management

Each player has a unique profile.

Example:

Player
────────────────────
Name
Date of birth
Position
Team
Parent/Guardian
Contact information
Registration information

A player is created independently from a team.

For example:

Create Player
      ↓
João Silva
      ↓
Create Team
      ↓
Petizes B
      ↓
Assign João → Petizes B

3. Staff Management

Staff members also have profiles.

Possible staff types:

Administrator
Head Coach
Assistant Coach
Other Staff

Staff can be associated with one or more teams depending on their role.

4. Teams

Administrators can create teams.

Example:

Petizes B
U9
2026/27

A team contains:

Team
 │
 ├── Players
 ├── Coaches
 ├── Training sessions
 ├── Matches
 └── Convocations
5. Seasons

The system should support different seasons.

For example:

2025/26
2026/27
2027/28

This allows us to keep historical information.

For example:

João Silva

2025/26 → Petizes A
2026/27 → Petizes B
2027/28 → Benjamins A
6. Player ↔ Team Assignment

Players aren't permanently attached to a team.

Instead, the system records their team assignment.

Player
   ↓
Team Assignment
   ↓
Team + Season

This allows the club to maintain a history of where each player played.

7. Training Management

Administrators/coaches can create training sessions.

Information:

Training
────────────────────
Team
Date
Start time
End time
Field
Coach

Example:

U13
Wednesday
18:30–19:30
Field 2
Coach Rui
8. Player Availability / Attendance

Parents can indicate whether their child will attend training.

Will Pedro attend?

YES
NO

The coach can then see:

Training — Wednesday

João       YES
Pedro      YES
Miguel     NO
André      YES

The system can also keep an attendance history.

9. Fields

The club can maintain a list of available fields.

Example:

Field 1
Field 2
Main Stadium
Training Pitch

Each training session or match can be associated with a field.

This also prevents scheduling conflicts later.

10. Matches

The system stores the club's matches.

Information:

Match
────────────────────
Team
Opponent
Date
Time
Location
Field
Competition
Home/Away
Score

11. Weekly Match Schedule

Users can see the upcoming matches.

For example:

THIS WEEK

Wednesday
U13 — Training
18:30

Saturday
U15 — Match
10:00

Sunday
U13 — Match
10:00

The schedule can be filtered by team.

12. Convocation System

At the end of the week, the coach creates the squad for the next match.

Example:

CONVOCATÓRIA

U13
Sunday — 10:00

Players:

✓ João
✓ Pedro
✓ Miguel
✓ André
✓ Ricardo

Meeting point:
09:15

Location:
Municipal Stadium

Parents can see the convocatória and potentially confirm their child's participation.

13. Calendar

The system has a central calendar containing:

Training
Matches
Convocations
Other club events

Example:

SEPTEMBER 2026

Monday
Training

Wednesday
Training

Saturday
Match

Sunday
Match

Clicking an event shows its details.

14. Messaging — Staff ↔ Parents

A private messaging system.

Coach
  ↕
Parent

Used for:

Training questions
Match information
Player availability
General communication
15. Messaging — Administrators ↔ Staff

Separate internal communication.

Administrator
      ↕
Staff

Administrators can communicate with:

Individual coaches
Specific teams
Multiple staff members
Potentially all staff
16. Notifications

Later, the system could notify users when something important happens.

For example:

New training scheduled
        ↓
Parent receives notification

New convocatoria
        ↓
Parent receives notification

Message received
        ↓
User receives notification

This can come later — it doesn't need to be part of the first version.

17. Calendar + Everything Connected

The important concept is that these aren't separate systems.

For example:

TEAM
 ↓
TRAINING
 ↓
FIELD
 ↓
PLAYERS
 ↓
ATTENDANCE
 ↓
PARENTS

And:

TEAM
 ↓
MATCH
 ↓
CONVOCATION
 ↓
PLAYERS
 ↓
PARENTS

And all of these appear in:

CALENDAR