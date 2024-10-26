from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import os
from dotenv import load_dotenv
from embedchain import App 
# Load environment variables
load_dotenv()

## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))





# Create your embedding model without OpenAI
app = App.from_config(config={"embedding_model": "gemini-1.5-flash"})





# create a senior blog content researchers

blog_reseachers = Agent(
                role = 'Blog Reseacher from youtube video',
                goal = 'get the relevant video content for the topic{topic} from the yt channel',
                verbose = True,
                memory = True,
                backstory = "Expert in understanding videos in AI Data Science , Machine Learning and GEN AI Solution",
                tools  = [yt_tool],
                llm = llm,
                allow_delegation = True
                
                
)


# creating a senior agent blog writer agent with yt tools

blog_writer = Agent(
              role = 'Blog writer',
              goal = "Narrate compelling tech stories about the videos {topic} from YT chaneel",
              verbose = True,
              memory = True,
              backstory = (
                          'With a flair for simplyfing complex topic , you craft'
                          "engaging narrative that captivate and educate , bringing new"
                          "discoveries to  light in an accessbile manner"
              ),
              
              tools = [yt_tool],
              llm = llm,
              allow_delegation = False
)