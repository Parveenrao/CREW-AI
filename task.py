from crewai import Task
from tools import yt_tool
from agents import blog_reseachers , blog_writer

# research task

reseach_task  = Task(
                description = (
                    'Identify the video {topic}'
                    'Get detailed information about the video from the channel'
                ),
                
                expected_output = 'A comprehensive 3 paragraph long report based on the {topic} of the video',
                tools = [yt_tool],
                agent = blog_reseachers
                
)


write_task = Task(
              description   = ('Get the info from the youtube channel  video on the topic'),
              expected_output = 'Summarize the info from the youtube channel video on the topic {topic}',
              tools = [yt_tool],
              agent = blog_writer,
              async_execution  = False,
              output_file = 'blog_post.md'
)