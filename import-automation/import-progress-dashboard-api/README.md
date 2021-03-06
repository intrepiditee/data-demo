# Import Progress Dashboard API

This directory contains code of a REST API that manages information
about import progress and logs.

# Data Model

There are three types of resources:
1. System Run
   - Describes a run of the executor
   - A system run can execute multiple import attempts each corresponding to
     an import specification in the manifest
   - See [app/model/system_run_model.py](app/model/system_run_model.py)
     for fields.
2. Import Attempt
   - An attempt to import a dataset executed by a system run
   - See [app/model/import_attempt_model.py](app/model/import_attempt_model.py)
     for fields.
3. Progress Log
   - A log generated by a system run and optionally an import attempt
   - See [app/model/progress_log_model.py](app/model/progress_log_model.py)
     for fields.

# Storage

The three types of entities are stored in Google Cloud Datastore. The message
bodies of progress logs are stored in Google Cloud Storage and loaded
dynamically when queried.

# Endpoints

1. `/system_runs` (See `SystemRunList` in
   [app/resource/system_run_list.py](app/resource/system_run_list.py))
   - Method: GET
   - Purpose: Filters system runs
   - Arguments
     - Any fields of a system run
   - URL parameters
     - `order`: List of field names to order the returned
       system runs by. Prepend "-" to a field name to sort it in
       descending order. The list is specified by repeated keys,
       e.g., `?order=status&order=-time_created`
     - `limit`: Maximum number of system runs to return, as an integer
   - Returns
     - List of system runs that pass the filter
2. `/system_runs`
   - Method: POST
   - Purpose: Creates a new system run
   - Arguments
     - Any fields of a system run except `run_id`, `import_attempts`, and `logs`
   - Returns
     - Created system run
3. `/system_runs/{run_id}` (See `SystemRunByID` in
   [app/resource/system_run.py](app/resource/system_run.py))
   - Method: GET
   - Purpose: Retrieves a system run by `run_id`
   - URL path variables
     - `run_id`: ID of the system run, as a string
   - Returns
     - System run with the `run_id`
4. `/system_runs/{run_id}` (See `SystemRunByID` in
   [app/resource/system_run.py](app/resource/system_run.py))
   - Method: PATCH
   - Purpose: Modifies an existing system run
   - Arguments:
     - Any fields of a system run except `run_id`, `import_attempts`, and `logs`
   - URL path variables
     - `run_id`: ID of the system run, as a string
   - Returns
     - Modified system run
5. `/system_runs/{run_id}/logs` (See `ProgressLogByRunID` in
   [app/resource/progress_log.py](app/resource/progress_log.py))
   - Method: GET
   - Purpose: Retrieves all the logs attached to a system run
   - URL path variables
     - `run_id`: ID of the system run, as a string
   - Returns
     - List of progress logs
6. `/import_attempts/{attempt_id}` (See `ImportAttemptByID` in
   [app/resource/import_attempt.py](app/resource/import_attempt.py))
   - Method: GET
   - Purpose: Retrieves an import attempt by `attempt_id`
   - URL path variables
     - `attempt_id`: ID of the import attempt, as a string
   - Returns
     - Import attempt with the `attempt_id`
7. `/import_attempts/{attempt_id}`
   - Method: PATCH
   - Purpose: Modifies an existing import attempt
   - Arguments:
     - Any fields of an import attempt except `attempt_id`, `run_id`, and `logs`
   - URL path variables
     - `attempt_id`: ID of the import attempt, as a string
   - Returns
     - Modified import attempt
8. `/import_attempts/{attempt_id}/logs` (See `ProgressLogByAttemptID` in
   [app/resource/progress_log.py](app/resource/progress_log.py))
   - Method: GET
   - Purpose: Retrieves all the logs attached to an import attempt
   - URL path variables
     - `attempt_id`: ID of the import attempt, as a string
   - Returns
     - List of progress logs
9. `/logs` (See `ProgressLogList` in [app/resource/progress_log_list.py](app/resource/progress_log_list.py))
   - Method: POST
   - Purpose: Creates a new progress log
   - Arguments
     - Any fields of a progress log except `log_id`
     - `message`, `level`, `run_id` are required
     - `attempt_id` can be optionally supplied to also attach the log to an
       import attempt
     - If `time_logged` is missing, the time at which the API receives the
       the request is used
   - Returns
     - Created progress log
10. `/logs/{log_id}` (See `ProgressLogByID` in [app/resource/progress_log.py](app/resource/progress_log.py))
   - Method: GET
   - Purpose: Retrieves a progress log by `log_id`
   - URL path variables
     - log_id: ID of the progress log, as a string
   - Returns
     - Progress log with the `log_id`


# Deploying to App Engine

1. Change [app/configs.py](app/configs.py) as appropriate
2. `gcloud app deploy`


# Running Tests

```
. run_test.sh
```

The Datastore emulator must be installed for the tests to run.
See https://cloud.google.com/datastore/docs/tools/datastore-emulator.
Running run_test.sh will attempt to install the emulator.
