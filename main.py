from jobs.jobs import Jobs

inst = Jobs()
inst.land_first_page()
inst.search_by_skills(skill="Python")
inst.search_by_skills_location(skill="Django", location="Mumbai")
inst.search_by_skills_location_experience(skill="Python", location="Tokyo", exp=2)
