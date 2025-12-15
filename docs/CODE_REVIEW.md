Code Review - Software Project



Review Type: Feature and Testing Review

Reviewed branches: feature/Testing, 

Target Branch: staging

Date: December 14, 2025

Reviewers: Muazam Syed, Mahendra Singh, Katie Reeves, Van Dong

Authors: Muazam Syed, Mahendra Singh, Katie Reeves, Van Dong





1\. Overview:



Summary of Changes made



This review covers the recent changes that were made related to testing, Docker configuration, CI/CD prep, and general project stabilization. The main focus of this reviewed work includes:



* Addition of automated tests for calculator endpoints(divide and multiply)
* Introduction of tests fixtures for consistent test data
* Fixes to incorrect test assumptions
* Resolution of a merge conflict caused by an out-of-date feature branch
* Prep for CI workflows to run tests automatically



-- The changes aim to improve code reliability, test coverage, and team workflow consistency.



2\. Code Review Findings:



Reviewed  Commit:

Step 3: Made changes to docker-compose.yml, Dockerfile, main.py, and …



Reviewed files:

* Dockerfile
* docker-compose.yml
* main.py



Observations:



* The Dockerfile was updated to use a non-root user, improving container security.
* Python version was updated to ensure compatibility with required libraries.
* Dependencies are now installed using requirements.txt(added), this improved consistency between local and container environments.
* There was a separate staging and productions services that was defined in docker-compose.yml.
* Health checks were also added for both environments to verify application availability.
* Environment Variables were introduced and correctly passed into the application.



Review Outcome:

Overall the changes improved security, created organization(addition of requirements.txt), clarity, and deployment reliability. The approach aligns well with CI/CD best practices and the project requirements.



Status: Approved, Pull request successfully merged and closed



2.2 Divide Tests (feature/Testing)



Reviewed Files:



* tests/test\_divide.py
* tests/fixtures/divide\_cases.json



Observations:



* Smoke test verifies that the /divide endpoint is reachable.
* Functional tests validate correct division behavior using fixture-based test data.
* Division-by-zero behavior is correctly handled and tested.
* A non-functional test verifies acceptable response time.
* Test structure and naming are clear and consistent.



Status: Approved, tests are running and everything is working





2.3 Multiply Tests (feature/multiply-tests)



Reviewed Files:



* tests/test\_multiply.py
* tests/fixtures/multiply\_cases.json



Issues Found:



* An initial test incorrectly treated multiplication by zero as an error case.
* Test naming initially referenced division instead of multiplication.



Resolution:



* The incorrect error-based test was removed or updated to reflect correct behavior.
* Multiplication by zero now correctly returns a successful response with a result of zero.
* Test naming was corrected for clarity.







Status: Approved after fixes



2.4 Merge Conflict Resolution



Issue:



* Code was pushed without pulling the latest changes from staging, causing a merge conflict.



Resolution:



* The conflict was manually resolved by reviewing file differences.
* Newly added test files, fixtures, and workflow-related changes were preserved.



The branch was successfully rebased and pushed after resolution.



Status: Resolved, testing files are functional



2.5 CI/CD and Workflow Files



Reviewed Files:



* .github/workflows/ci.yml



* .github/workflows/staging.yml



* .github/workflows/production.yml



Observations:



* Workflow files are present and correctly organized.
* CI is configured to run automated tests using pytest.



Status: Complete, the workflow files are running in GitHub actions page



3\. General Code Quality Assessment



* Code changes are focused and relevant.
* Tests are consistent across endpoints.
* Use of fixtures improves maintainability.
* No sensitive information was introduced.
* Code follows project conventions.



4\. Required Actions in GitHub



To complete governance requirements:



&nbsp;	1. Create GitHub issues documenting:



* Initial incorrect multiply-by-zero test assumption
* Merge conflict caused by outdated feature branch
* Final review and validation of CI workflows



&nbsp;	2. Link issues to pull requests using references such as Fixes #<issue-number>.



&nbsp;	3. Ensure pull requests include at least one reviewer approval.



&nbsp;	4. Merge approved changes into the staging branch





5\. Final Review Decision



Decision: Approved



The reviewed changes improve application stability, testing coverage, and deployment reliability. Identified issues were addressed, and the project is ready to proceed with its next phases.



Reviewer Signature: Muazam Syed
Date: December 14, 2025

