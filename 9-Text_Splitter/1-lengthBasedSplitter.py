from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader




loader = PyPDFLoader('Docker.pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size =200,
    chunk_overlap =0,
    separator = ""
)

# chunk Overlap: 
# For RAG Based Applications : 10-20

text = """Space technology refers to the tools, machines, and techniques developed to explore and utilize outer space. This field has grown immensely since the launch of Sputnik 1 by the Soviet Union in 1957, which marked the beginning of the space age. Today, space technology plays a crucial role in communication, navigation, weather forecasting, defense, scientific research, and even daily life. It includes satellites, space telescopes, launch vehicles, space stations, rovers, and other systems designed for space exploration and utilization. One of the most common examples of space technology in our daily life is the GPS in our mobile phones. These systems rely on a network of satellites orbiting the Earth to provide precise location information, showing how space innovations directly impact our lives.

Space agencies like NASA, ISRO, ESA, and SpaceX are constantly pushing boundaries. For instance, India's Mars Orbiter Mission (Mangalyaan) became famous worldwide for being one of the most cost-effective Mars missions ever. SpaceX, a private company, has revolutionized the industry by creating reusable rockets, significantly reducing the cost of space travel. These advancements have opened new doors for commercial space exploration, including plans for space tourism, Moon bases, and even manned missions to Mars. The James Webb Space Telescope, launched in 2021, is another example of how advanced space technology can help scientists study the formation of stars, galaxies, and possibly life on other planets.

Space technology also helps monitor and protect our planet. Earth observation satellites provide real-time data about deforestation, climate change, natural disasters, and agricultural patterns. During floods or cyclones, satellite images help governments plan rescue operations and distribute aid more efficiently. In agriculture, satellite data helps farmers predict rainfall, detect soil moisture, and improve crop planning. Space technology is also essential in global communication. Satellite networks support mobile phones, internet, and TV broadcasting, enabling us to connect across continents in seconds."""

# result = splitter.split_text(text)
result = splitter.split_documents(docs)

print(result[0].page_content)