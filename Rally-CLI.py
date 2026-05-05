from pyral import Rally
import getpass

password = getpass.getpass("Enter your Rally password: ")

rally = Rally(
    server='rally1.rallydev.com',
    user='vous@votrecompanie.com',
    password=password
)

# Get recent stories
response = rally.get('UserStory', 
    fetch='FormattedID,Name,ScheduleState,Owner',
    order='LastUpdateDate DESC',
    limit=30
)

print(f"Recent stories ({response.resultCount} found):\n")

for story in response:
    owner = "Unassigned"
    if story.Owner:
        owner = story.Owner.DisplayName
    
    print(f"{story.FormattedID}: {story.Name}")
    print(f"  Owner: {owner}")
    print(f"  State: {story.ScheduleState}\n")
	
	