from models.user import User
from utils.storage import save_data

user = User("Newton", "newton@example.com")

save_data(
    "data/users.json",
    [user.to_dict()]
)

print("User saved successfully")