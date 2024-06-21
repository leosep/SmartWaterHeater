def return_skill():
    # Import the actual skill logic
    from alexa_skill import skill
    app = skill.create_skill()
    return app