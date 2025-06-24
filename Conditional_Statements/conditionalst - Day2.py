
# Used heavily in DevOps automation scripts, e.g., to check server health, decide actions on response codes, alert thresholds.
#What are Conditional Statements? Conditional statements in Python let you execute code based on conditions (True/False). Used in automation, deployment logic, status checks, etc.
# if condition:
#     # code block
# elif another_condition:
#     # another block
# else:
#     # fallback


#Simple IF :

status = "success"

if status == "success":
    print("Deployment completed!")
    

#if-else :

cpu_usage = 85

if cpu_usage > 80:
    print("High CPU usage! Alert!")
else:
    print("CPU usage is normal.")

#if-elif-else :

http_code = 503

if http_code == 200:
    print("OK")
elif http_code == 404:
    print("Not Found")
elif http_code == 503:
    print("Service Unavailable")
else:
    print("Unhandled response")

#Nested if :

region = "us-east-1"
instance_state = "running"

if region == "us-east-1":
    if instance_state == "running":
        print("Instance is up in US-East.")

