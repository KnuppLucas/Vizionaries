from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from joblib import dump

dados_rotulados = [
    {"texto": "Global climate change has rippling effects on our environment, impacting where plants, animals, and humans can live. The USGS studies how climate change affects natural places and provides solutions to help protect fish, wildlife, and habitats.", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Everything in the natural world is connected. Animals eat plants, insects pollinate flowers, microbes break down dead things. Living things are also connected to the “non-living” parts of their environments they use rocks for shelter, they depend on rain to bloom, they hibernate when it gets cold. Together, these living and non-living components make up an ecosystem.", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Climate helps shape ecosystems. Things like average temperatures, humidity, and rainfall determine where plants and animals live. If a regions climate changes, the ecosystems change as well.", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Model species range shifts under potential future conditions", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Identify species particularly vulnerable to climate change", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Identify areas relatively buffered from climate change (“climate refugia”) that may help vulnerable species survive", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Potential effects of climate change on snail kites (Rostrhamus sociabilis plumbeus) in Florida The snail kite (Rostrhamus sociabilis plumbeus), an endangered, wetland-dependent raptor, is highly sensitive to changes in hydrology. Climate-driven changes in water level will likely affect snail kite populations—altering reproductive success and survival rates. Identifying the mechanisms mediating the direct and indirect effects of climate on snail kite populations and the range of future climaAuthorsMarta P. Lyons, Olivia E. LeDee, Ryan Boyles", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Conservation under uncertainty: Innovations in participatory climate change scenario planning from U.S. national parks The impacts of climate change (CC) on natural and cultural resources are far-reaching and complex. A major challenge facing resource managers is not knowing the exact timing and nature of those impacts. To confront this problem, scientists, adaptation specialists, and resource managers have begun to use scenario planning (SP). This structured process identifies a small set of scenarios—descriptionAuthorsBrian W. Miller, Gregor W. Schuurman, Amy Symstad, Amber C Runyon, Brecken C. RobbByEcosystems Mission Area, Climate Adaptation Science Centers, Northern Prairie Wildlife Research Center", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "The impact of future climate on wetland habitat in a critical migratory waterfowl corridor of the Prairie Pothole Region Depressional wetlands are extremely sensitive to changes in temperature and precipitation, so understanding how wetland inundation dynamics respond to changes in climate is essential for describing potential effects on wildlife breeding habitat. Millions of depressional basins make up the largest wetland complex in North America known as the Prairie Pothole Region (PPR). The wetland ecosystems thaAuthorsOwen P. McKennaByEcosystems Mission Area, Climate Research and Development Program, Northern Prairie Wildlife Research Center", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Stoneflies in the genus Lednia (Plecoptera: Nemouridae): Sentinels of climate change impacts on mountain stream biodiversity Rapid recession of glaciers and snowfields is threatening the habitats of cold-water biodiversity worldwide. In many ice-sourced headwaters of western North America, stoneflies in the genusLednia(Plecoptera: Nemouridae) are a prominent member of the invertebrate community. With a broad distribution in mountain streams and close ties to declining glacier cover,Lednia has emerged as a sentinel ofAuthorsMatthew D. Green, Lusha M. Tronstad, J. Joseph Giersch, Alisha A. Shah, Candace E. Fallon, Emilie Blevins, Taylor Kai, Clint C. Muhlfeld, Debra S. Finn, Scott HotalingByEcosystems Mission Area, Cooperative Research Units, Northern Rocky Mountain Science Center", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Long-term variation in polar bear body condition and maternal investment relative to a changing environment In the Arctic, warming air and ocean temperatures have resulted in substantial changes to sea ice, which is primary habitat for polar bears (Ursus maritimus). Reductions in extent, duration, and thickness have altered sea ice dynamics, which influences the ability of polar bears to reliably access marine mammal prey. Because nutritional condition is closely linked to population vital rates, a progAuthorsTodd C. Atwood, Karyn D. Rode, David C. Douglas, Kristin S. Simac, Anthony Pagano, Jeffrey F. BromaghinByEcosystems Mission Area, Alaska Science Center", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Response of forage plants to alteration of temperature and spring thaw date: Implications for geese in a warming Arctic Changes in summer temperatures in Arctic Alaska have led to longer and warmer growing seasons over the last three decades. Corresponding with these changes in climate, the abundance and distributions of geese have increased and expanded over the same period. We used an experimental approach to assess the response of goose forage plants to simulated environmental change. We subjected Carex subspathAuthorsPaul L. Flint, Brandt W. MeixellByEcosystems Mission Area, Land Management Research Program, Alaska Science Center", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Reduced quality and synchronous collapse of forage species disrupts trophic transfer during a prolonged marine heatwave The Gulf of Alaska forage fish community includes a few key species that differ markedly in their timing of spawning, somatic growth and lipid storage, and in their migration behavior. This diversity in life history strategies facilitates resilience in marine food webs because it buffers predators against the naturally high variance in abundance of pelagic forage fish populations by decreasing theAuthorsMayumi L. Arimitsu, John F. Piatt, Scott Hatch, Rob Suryan, Sonia Batten, Mary Anne Bishop, Rob Campbell, Heather Coletti, Dan Cushing, Kristen Gorman, Stormy Haught, Russell Hopcroft, Kathy Kuletz, Caitlin Elizabeth Marsteller, Caitlin McKinstry, David McGowan, John Moran, R. Scott Pegau, Anne Schaefer, Sarah K. Schoen, Jan Straley, Vanessa R. von BielaByEcosystems Mission Area, Land Management Research Program, Alaska Science Center", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "Resist-Accept-Direct (RAD) Framework The Resist-Accept-Direct (RAD) framework is a decision-making tool that helps resource managers make informed strategies for responding to ecological changes resulting from climate change.ByClimate Adaptation Science Centerslink September 26, 2023  Resist-Accept-Direct (RAD) FrameworkThe Resist-Accept-Direct (RAD) framework is a decision-making tool that helps resource managers make informed strategies for responding to ecological changes resulting from climate change", "categoria": "society", "agencia":"SEDAC", "topico": "vulnerabilities"},
    {"texto": "“Greenhouse” gases occur naturally in the Earths atmosphere. They help regulate the planets temperature, like how the glass in a greenhouse retains heat or a blanket reflects your body heat to keep you warm. Adding more greenhouse gases into the atmosphere, like we do when burning fossil fuels, acts like putting a thicker blanket on the planet. The thicker the blanket of greenhouse gases, the less heat escapes into space. This causes the planet to get warmer.", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    
    {"texto": "There are also natural sources of greenhouse gases, including volcanic eruptions, geologic seeps from features like hot springs and geothermal vents, thawing permafrost, and forest fires. Climate change and human activities can accelerate natural emissions. Warmer temperatures defrost permafrost and heat up oceans, releasing the carbon long stored in these systems. Wetlands drained for agriculture can rapidly switch from being carbon sinks to being carbon sources. And human ignitions and climate-driven dryness mean long, intense fire seasons, releasing billions of metric tons of carbon dioxide around the world each year.", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    {"texto": "The main contributor to climate change is human emissions. Although the greenhouse gases responsible for causing climate change do occur naturally in our atmosphere, the concentrations have been increasing significantly since the 1880s. The increase in the amount of carbon dioxide, in particular, is the biggest culprit that has led to a 1.9-degrees Fahrenheit in the planets average global temperature since the Industrial Revolution.", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    {"texto": "One characteristic of climate change that continues to evolve is how we discuss the different factors that contribute to it. Historically, the burning of fossils fuels was the primary focus, as that is the key driver of increased greenhouse gases, particularly carbon. However, as researchers learn more about the ways carbon cycles through the atmosphere, a more nuanced picture is beginning to form. Scientists use color to classify carbon at different points in the carbon cycle based on carbon function, characteristics, and location. This creates a more descriptive framework than traditional organic and inorganic labels - a carbon rainbow, so to speak.""The Colors of Carbon include:", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    {"texto": "Sometimes people may be confused by the difference between weather and climate. A single snowstorm or cold spell does not disprove global warming. Weather refers to short-term atmospheric conditions, while climate is the weather of a specific region averaged over a long period of time. While we expect the weather to change almost daily, a regions climate is normally stable over time. For example, Florida is generally warmer and rainier than Montana, even if on a particular day it is raining in Montana but not in Florida. Climate change refers to long-term changes in a regions climate. In recent years, parts of the country are frequently experiencing higher temperatures than they used to, like regular 100-degree days in Colorado that used to be an extreme outlier. Places are also seeing weather patterns that are completely out of sync with their historical climate. In fact, a consequence of climate change is more erratic weather patterns, including wild snowstorms and anomalies like the polar vortex reaching farther south or a heatwave in the Pacific Northwest that rivals temperatures typically seen in Death Valley, California.", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    {"texto": "Global warming. Climate change. Climate crisis. No matter how you refer to the threat, they are all related. The average temperature of the Earths surface has increased significantly since the 1880s (i.e., global warming). This has led to significant changes to the long-term weather patterns, or climate, of regions across the globe (i.e., climate change). And due to the consequences of climate change (e.g., drought, flooding, melting sea ice, disease, etc.), some consider the threat a genuine global crisis (i.e., climate crisis). No matter what we call it, the science is clear that our world is changing because of increased greenhouse gases in the atmosphere", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    {"texto": "USGS science particularly focuses on helping resource managers, conservation agencies, and Indigenous peoples implement climate adaptation practices that intentionally help preserve species and landscapes under new climate conditions. For example, this could involve building sea walls to keep out rising sea levels, or planting drought-tolerant grasses in dry areas. Adapted landscapes may not look exactly the way they used to, but ideally the modifications allow them to continue to support the natural and human communities that rely on them. USGS scientists also use monitoring, field work, and modeling to understand how species naturally adapt to climate change, called adaptive capacity.", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    {"texto": "The USGS One Health Approach to WildLife Disease and Environmental Change, is a collaborative approach working at the local, regional, national, and global levels with the goal of achieving optimal health...", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    {"texto": "Scientists at the USGS study how climate change affects the Nations wildlife, fish, plants, and ecosystems. We also help resource managers develop and implement strategies to allow plants and animals to survive and thrive in new conditions. We generate our science side-by-side with partners to ensure results and tools are directly applicable to on-the-ground conservation, restoration, and management decisions. USGS climate science is used to protect natural areas across the country, from local-scale conservation decisions to national park climate scenario planning.", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},


    {"texto": "How can climate change affect natural disasters? With increasing global surface temperatures the possibility of more droughts and increased intensity of storms will likely occur. As more water vapor is evaporated into the atmosphere it becomes fuel for more powerful storms to develop. More heat in the atmosphere and warmer ocean surface temperatures can lead to increased wind speeds in tropical storms. Rising sea levels expose higher locations...link  How can climate change affect natural disasters? With increasing global surface temperatures the possibility of more droughts and increased intensity of storms will likely occur. As more water vapor is evaporated into the atmosphere it becomes fuel for more powerful storms to develop. More heat in the atmosphere and warmer ocean surface temperatures can lead to increased wind speeds in tropical storms. Rising sea levels expose higher locations...", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    {"texto": "What are some of the signs of climate change? • Temperatures are rising world-wide due to greenhouse gases trapping more heat in the atmosphere.• Droughts are becoming longer and more extreme around the world.• Tropical storms becoming more severe due to warmer ocean water temperatures.• As temperatures rise there is less snowpack in mountain ranges and polar areas and the snow melts faster.• Overall, glaciers are melting at a faster rate.•...link  What are some of the signs of climate change? • Temperatures are rising world-wide due to greenhouse gases trapping more heat in the atmosphere.• Droughts are becoming longer and more extreme around the world.• Tropical storms becoming more severe due to warmer ocean water temperatures.• As temperatures rise there is less snowpack in mountain ranges and polar areas and the snow melts faster.• Overall, glaciers are melting at a faster rate.", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    {"texto": "What are the long-term effects of climate change? Scientists have predicted that long-term effects of climate change will include a decrease in sea ice and an increase in permafrost thawing, an increase in heat waves and heavy precipitation, and decreased water resources in semi-arid regions. Below are some of the regional impacts of global change forecast by the Intergovernmental Panel on Climate Change: North America: Decreasing snowpack in the...link  What are the long-term effects of climate change? Scientists have predicted that long-term effects of climate change will include a decrease in sea ice and an increase in permafrost thawing, an increase in heat waves and heavy precipitation, and decreased water resources in semi-arid regions. Below are some of the regional impacts of global change forecast by the Intergovernmental Panel on Climate Change: North America: Decreasing snowpack in the...", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    {"texto": "What is the difference between global warming and climate change? Although people tend to use these terms interchangeably, global warming is just one aspect of climate change. “Global warming” refers to the rise in global temperatures due mainly to the increasing concentrations of greenhouse gases in the atmosphere. “Climate change” refers to the increasing changes in the measures of climate over a long period of time including precipitation, temperature, and...link  What is the difference between global warming and climate change? Although people tend to use these terms interchangeably, global warming is just one aspect of climate change. “Global warming” refers to the rise in global temperatures due mainly to the increasing concentrations of greenhouse gases in the atmosphere. “Climate change” refers to the increasing changes in the measures of climate over a long period of time including precipitation, temperature, and...Learn More", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},
    {"texto": "The impacts of a changing climate on wildlife and associated ecosystems have yet to be fully determined but changes are clearly underway as are a variety of investigations to assess how we can best preserve key resources while effectively managing others. Using a variety of tools and a combination of studies including adaptive management, long-term monitoring, mathematical modeling, and...link April 9, 2018  Climate ChangeThe impacts of a changing climate on wildlife and associated ecosystems have yet to be fully determined but changes are clearly underway as are a variety of investigations to assess how we can best preserve key resources while effectively managing others. Using a variety of tools and a combination of studies including adaptive management, long-term monitoring, mathematical modeling, and...", "categoria": "climate", "agencia":"USGS", "topico": "climate-change-101"},

    {"texto": "An Ecosystem of Minority Health and Health Disparities Resources", "categoria": "health", "agencia":"NIH", "topico": "ecosistema"},
    {"texto": "Recognizing the need for high-quality, publicly available online resources for improving minority health and reducing health disparities, NIMHD developed HDPulse.", "categoria": "health", "agencia":"NIH", "topico": "ecosistema"},
    {"texto": "Researchers in academic institutions, research organizations, or federal organizationsPublic health practitioners (program implementers)Healthcare providers (clinicians, nurses, behavioral health providers)", "categoria": "health", "agencia":"NIH", "topico": "ecosistema"},
    {"texto": "Purpose: Provides a tool to characterize health disparities to motivate action to reduce health disparities. Interactive graphics and maps provide visual support for deciding where to focus public health disparities control efforts.", "categoria": "health", "agencia":"NIH", "topico": "ecosistema"},
    {"texto": "The Data Portal offers quick, easy access to descriptive statistics, interactive graphics, and maps that present health disparities across the nation, states and counties. With easy navigation and a mobile-friendly interface that offers several ways to view and download health disparity data, the portal will provide opportunities to explore health disparity topics such as screening and risk factors, socio-demographics, and mortality—with more to come!", "categoria": "health", "agencia":"NIH", "topico": "ecosistema"},
    {"texto": "Purpose: Provides easy access to interventions that have demonstrated effect to improve minority health or reduce health disparities, along with related publications, products and materials.", "categoria": "health", "agencia":"NIH", "topico": "ecosistema"},
    {"texto": "The Interventions Portal can inform the design, implementation, evaluation, dissemination, and adaptation of interventions to improve minority health and reduce health disparities. Minority health and health disparities researchers, program planners, and intervention developers can submit, find, sort, and download evidence-based interventions and resources. Coming soon!", "categoria": "health", "agencia":"NIH", "topico": "ecosistema"},
    
    {"texto": "American Meteorological Society Graduate Fellowship", "categoria": "meteorological", "agencia":"NOAA", "topico": "research"},
    {"texto": "Applicants must be seeking degrees in the fields of atmospheric sciences, chemistry, computer sciences, engineering, environmental sciences, hydrology, mathematics, oceanography, and physics. NOAA's Climate Program Office provides funding to support three AMS graduate fellows per year.", "categoria": "meteorological", "agencia":"NOAA", "topico": "research"},
    {"texto": "he NOAA Central Library offers a wide variety of internship and volunteer opportunities for students interested in library sciences, information management, or NOAA's mission.", "categoria": "meteorological", "agencia":"NOAA", "topico": "research"},
    {"texto": "They have a variety of projects that will help students develop research, analytic, and technical skills.", "categoria": "meteorological", "agencia":"NOAA", "topico": "research"},
    {"texto": "Chesapeake Bay Summer Internship Program", "categoria": "meteorological", "agencia":"NOAA", "topico": "research"},
    {"texto": "Each summer, NOAA Chesapeake Bay Office, in partnership with the Chesapeake Research Consortium, offers several paid summer internships primarily geared toward current undergraduate students. Internships focus on scientific field research to resource management and policy.", "categoria": "meteorological", "agencia":"NOAA", "topico": "research"},
    {"texto": "CRC Chesapeake Student Recruitment, Early Advisement, and Mentoring (C-StREAM) program is focused on recruiting, advising, and mentoring college students from populations who have been historically excluded from the environmental field and are underrepresented in environmental research and management professions.", "categoria": "meteorological", "agencia":"NOAA", "topico": "research"},
    {"texto": "For the purpose of this program, C-StREAM focuses on assisting students who identify as people of color and/or who are first generation college students.", "categoria": "meteorological", "agencia":"NOAA", "topico": "research"},
    
    {"texto": "Americans have clean air, land and water;", "categoria": "environment", "agencia":"EPA", "topico": "ambiente"},
    {"texto": "National efforts to reduce environmental risks are based on the best available scientific information", "categoria": "environment", "agencia":"EPA", "topico": "ambiente"},
    {"texto": "Federal laws protecting human health and the environment are administered and enforced fairly, effectively and as Congress intended;", "categoria": "environment", "agencia":"EPA", "topico": "ambiente"},
    {"texto": "Environmental stewardship is integral to U.S. policies concerning natural resources, human health, economic growth, energy, transportation, agriculture, industry, and international trade, and these factors are similarly considered in establishing environmental policy;", "categoria": "environment", "agencia":"EPA", "topico": "ambiente"},
    {"texto": "All parts of society--communities, individuals, businesses, and state, local and tribal governments--have access to accurate information sufficient to effectively participate in managing human health and environmental risks;", "categoria": "environment", "agencia":"EPA", "topico": "ambiente"},
    {"texto": "Contaminated lands and toxic sites are cleaned up by potentially responsible parties and revitalized; and", "categoria": "environment", "agencia":"EPA", "topico": "ambiente"},
    {"texto": "Chemicals in the marketplace are reviewed for safety.", "categoria": "environment", "agencia":"EPA", "topico": "ambiente"},
    {"texto": "When Congress writes an environmental law, we implement it by writing regulations.", "categoria": "environment", "agencia":"EPA", "topico": "ambiente"},
    {"texto": "Often, we set national standards that states and tribes enforce through their own regulations. If they fail to meet the national standards, we can help them. We also enforce our regulations, and help companies understand the requirements.", "categoria": "environment", "agencia":"EPA", "topico": "ambiente"},
    {"texto": "At laboratories located throughout the nation, we identify and try to solve environmental problems. To learn even more, we share information with other countries, private sector organizations, academic institutions, and other agencies.", "categoria": "environment", "agencia":"EPA", "topico": "ambiente"},

]

textos = [item["texto"] for item in dados_rotulados]
categorias = [item["categoria"] for item in dados_rotulados]
agencias = [item["agencia"] for item in dados_rotulados]
topicos = [item["topico"] for item in dados_rotulados]

vetorizador = TfidfVectorizer()
X = vetorizador.fit_transform(textos)

modelo_categoria = MultinomialNB()
modelo_categoria.fit(X, categorias)

modelo_agencia = MultinomialNB()
modelo_agencia.fit(X, agencias)

modelo_topico = MultinomialNB()
modelo_topico.fit(X, topicos)

def fazer_previsao(frase):
    frase_preprocessada = preprocessar_frase(frase)
    
    vetor_frase = vetorizador.transform([frase_preprocessada])
    
    categoria_predita = modelo_categoria.predict(vetor_frase)
    agencia_predita = modelo_agencia.predict(vetor_frase)
    topico_predito = modelo_topico.predict(vetor_frase)
    
    return categoria_predita, agencia_predita, topico_predito

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

def preprocessar_frase(frase):
    tokens = word_tokenize(frase)
    
    tokens = [token.lower() for token in tokens]
    
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    frase_processada = ' '.join(tokens)
    
    return frase_processada

user_input = "SEDAC humanity vulnerability"
categoria_predita, agencia_predita, topico_predito = fazer_previsao(user_input)


dump(modelo_categoria, 'modelo_categoria.joblib')
dump(modelo_agencia, 'modelo_agencia.joblib')
dump(modelo_topico, 'modelo_topico.joblib')
dump(vetorizador, 'vetorizador.joblib')

print("User input:", user_input)
print("Category:", categoria_predita)
print("Agency:", agencia_predita)
print("Topic:", topico_predito)