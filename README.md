# Vizionaries
Welcome to the Vizionaries Project
This project was created for the Hackathon NASA Space Apps 2023, in response to the challenge: "Mapping Data for Societal Benefit."

## Summary
In a world where complex challenges such as climate change, poverty, water and food insecurity, and diseases threaten our planet, we recognize that scientists and data analysts cannot tackle these issues alone. We need individuals from all fields and backgrounds to engage with this data, contribute insights, and collaborate as a global task force.

We have developed a revolutionary platform with the central mission of democratizing access to NASA's and other federal agencies' open data. Through advanced techniques like web scraping and artificial intelligence, we have made this data more accessible and comprehensible through intuitive visualizations.

Our core vision is to expand the number of people who can access this data, making it easily accessible and understandable for everyone, not just scientists and analysts. We understand that simplifying access to and comprehension of this data fosters a global community of citizen scientists united in addressing the urgent challenges facing our planet. Together, we can work towards advancing the Sustainable Development Goals agenda.

To illustrate, we demonstrate how our solution simplifies data retrieval through web scraping and AI, and we present an intuitive visualization that highlights a country's vulnerability to physical hazards while emphasizing regional disparities.

This is the essence of the Vizionaries Project: democratize data and create a global community committed to a more sustainable and data-driven future.

## Our Greatest Motivation
Our greatest motivation lies in harnessing collective effort. We believe that to generate the necessary strength to confront global challenges, we need to bring together a 'mass' of individuals from non-scientific backgrounds, working together and driving progress with their diverse perspectives and skills. Our formula for success is clear: a larger 'mass' multiplied by the 'acceleration' of ideas and actions results in an unstoppable force for change.

## Our Code
Our frontend was built on Wixx, a no-code platform.

However, our primary focus has been on developing the backend of the application.

We've trained an AI responsible for integrating with the search input on the project's home page. Based on the input, the AI interprets it and provides information about the relevant agency, topic, and category for the search. For example, when conducting a search related to "Sedac vulnerability research," the AI would return that the associated agency is SEBAC, the topic is society, and the category is vulnerability. Subsequently, the AI calls a procedure in the database to retrieve all related files found in our database, resulting in an efficient search. We've trained the AI with data from various agencies, enabling it to conduct more efficient and secure searches.

To populate the AI's data catalog, we employed web scraping techniques on agency webpages, ensuring that the information remains current in line with the respective websites.

We've also developed an AI capable of generating graphs. The test files are available in this repository.

We've created a 3D visualization globe using the Globe.gl library, which offers an excellent visual representation of data. To populate the globe, we conducted research, data analysis, and treatment, populating a geojson file to ensure optimal functionality.

This is the commitment of the Vizionaries Project: democratizing data and uniting a global community dedicated to building a more sustainable and data-driven future.

![image](https://github.com/KnuppLucas/Vizionaries/assets/102392874/afa2564c-4146-45c8-b328-4cedc8035196)

![image](https://github.com/KnuppLucas/Vizionaries/assets/102392874/da1fe612-9ce5-4398-862c-b7c14b152dec)

![image](https://github.com/KnuppLucas/Vizionaries/assets/102392874/64ccdb4d-3ed3-444d-ba02-a765e5c10c4b)

![image](https://github.com/KnuppLucas/Vizionaries/assets/102392874/74ee61be-bdbe-411a-b838-559334105a97)

