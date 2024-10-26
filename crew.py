from  crewai import Process , Crew
from agents import blog_reseachers , blog_writer
from tools import yt_tool
from task import reseach_task , write_task

crew = Crew(
       agents = (blog_reseachers , blog_writer),
       tasks = (reseach_task , write_task),
       process  = Process.sequential,
       memory = True,
       share_crew = True,
       cache = True,
       max_rpm = 100
       
)


result  = crew.kickoff(inputs = {'topic':'AI VS ML vs DL vs Data Science'})

