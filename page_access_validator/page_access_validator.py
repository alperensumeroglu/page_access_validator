def permission_check(page):
    # Define role permissions
    role_permissions = {
        'Admin': ['Product Edit', 'User Management', 'Dashboard'],
        'User': ['Dashboard', 'Profile'],
        'Guest': ['Home']
    }
    # Determine all valid pages
    valid_pages = set(page for pages in role_permissions.values() for page in pages)
    # Inner function to check permissions
    def inner(role):
        # Check if the role is valid
        if role not in role_permissions:
            return f'Invalid role: {role}. Valid roles: {", ".join(role_permissions.keys())}'
        # Check if the page is valid
        if page not in valid_pages:
            return f"Invalid page: {page}. Valid pages: {', '.join(valid_pages)}"
        # Check if the role can access the page
        if page in role_permissions.get(role, []):
            return f"{role} role can access the {page} page."
        else:
            return f"{role} cannot access the {page} page."
    return inner
#Test the function
def test_permission_check():
    # Create the permission checker function for a specific page
    page = input('Enter the page to check access for (Product Edit, User Management, Dashboard, Profile, Home): ')
    permission_checker = permission_check(page)
    #Get role from user and check access
    role = input('Enter the role to check access(Admin, User, Guest): ')
    result = permission_checker(role)
    print(result)
test_permission_check()