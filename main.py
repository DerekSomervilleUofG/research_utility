from utility.Communication import Communication

communication = Communication()
communication.send_ms_team_message("Del sent message")
communication.send_email("derek.somerville@glasgow.ac.uk", "TEST", "Test message")