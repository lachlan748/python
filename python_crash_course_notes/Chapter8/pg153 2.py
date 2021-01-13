def build_profile(first, last, **user_info):
    # Build a dict containing information about a given user
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile

user1_profile = build_profile('roger', 'federer',
                             nationality = 'swiss',
                             field = 'tennis')

user2_profile = build_profile('ivan', 'lendl',
                             nationality = 'czech',
                             field = 'tennis')

print(user1_profile)
print(user2_profile)
