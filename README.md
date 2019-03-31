# Tour-Distributor
## Solution details
Implementation of our solution will be web-based application.
Core elements of application:
Backend is REST service implemented as flask application; mongoDB for employees personal information storage
Frontend is react application with multiple pages: priority queue, application, etc

### EMPLOYEE EXPERIENCE
Two web-views are available to employee:
 * Submitting vacation tour form. Employee submits his table number and vacation tour type and details. Inside, our backend extracts features from database for current employee, calculate “score” value, which defines how big chances for getting a vacation tour are, and puts score to database
 * Search for employee in current site’s (location) rating form. Employee can type his table number and see his position among other employees (in a list of employees sorted by score). He also can see if he currently passes or not. (e.g., you have 80 tours, and employee is 67th in rating, so he passes at this moment). In real world, each time employee’s feature value changed (e.g., new children is born), score should-be recalculated. Plus, if employee’s position in rating is changed (many different events can cause it), he’s notified about it with new email.  
Additional 2nd priority feature: user can click on his row in a list of employees, and he should see what can be done to get higher in rating (work better for getting rewards, continue work to increase experience, etc.)

### CORE BACKEND PART
Task of distribution tours between employees can be solved by using formula to compute weighted combination (possibly, non-linear) of features that can be taken from presented datasets, and maybe more.  
We decided to start with simple model (basically it’s just mathematical expression) which uses following features:  

Additive:
 * Single Parent: single_parent
 * Guardian: guardian
 * Children count: children_count
 * Best in profession competition (1st, 2nd or 3rd place): best_member
 * Corporate rewards for the last two years: rewards
 * Experience: experience  

Multiplicative:
 * Years from last vacation
 * Disciplinary sanction

All additive features can be taken from excel datasets with some basic pre-processing (e.g., count the number of children of employee, define who are under 18, and produce final count, etc.). The only multiplicative value is not presented in current datasets, but we want it to have there. It is useful to multiply score of employees who haven’t got a vacation tour for a long time. That means that even employees with lower performance/visibility results eventually will get the rest for them & family.

For each employee that wants to get a tour, and for each type of tour (currently two of them: child-only and family), we compute special value we call “score” depending on values for each feature we take into account. The simplest model looks like this:

<b>SCORE</b> = mw1 * mx1 * … * mwn * mxn * (aw1 * ax1 + … + awk * axk) / k, where:
 * mwi - weight of mxi
 * mxi - value of i-th multiplicative feature (e.g. years from last vacation = 4)
 * awi - weight of axi
 * axi - value of i-th additive feature (e.g. children count = 3)
 * n - total number of multiplicative features (in our first version = 1)
 * k - total number of additive features (in our first version = 4 for child-only vacation  and 6 for family)

Each wi * xi multiplication will result into value from 0 to 1 due to force xi value crop before computing score value. For example, weight for experience equals to 1/10. This means that maximum profit that employee can get from his experience (years he worked for SIBUR) equals to 10. If employee have been working here for 10 years or more, this value is force cropped to 10, and employee gets w * x equal to 1 (maximum for current feature).


## List of features to use [WIP]
 * Additive:
   * Single Parent: single_parent
   * Guardian: guardian
   * Children count: children_count
   * Best in profession competition (1st, 2nd or 3rd place): best_member
   * Corporate rewards for the last two years: rewards
   * Experience: experience
 * Multiplicative:
   * Years from last vacation: prev_vacations
   * Disciplinary sanction: disciplinary_sanction
