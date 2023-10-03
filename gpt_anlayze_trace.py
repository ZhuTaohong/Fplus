import subprocess
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate, StringPromptTemplate
from langchain.memory import ConversationBufferMemory
from pydantic import BaseModel, validator
import os

PROMPT = """\
Given the trace and source code.
Source Code:
{source_code}
Trace:
{trace}

Analyze:
"""

template = """You are a debug tool, now receiving program source code and trace.

{chat_history}
Human: {human_input}
"""

fix_prompt = """

Only according to the Trace and analyze from GPT to fix the program where has errors，so that the program will not terminate abnormally.

Do not give me document format

Just give the fixed program to me without any explanation

#fixed program code are followed

"""


class CrashesExplainerPromptTemplate(StringPromptTemplate, BaseModel):

    def format(self, **kwargs) -> str:
        # Generate the prompt to be sent to the language model
        prompt = PROMPT.format(
            source_code=kwargs["source_code"], trace=kwargs["trace"]
        )
        return prompt

    def _prompt_type(self):
        return "crashes-explainer"


def crash_analyze(code_path):
    code_name = os.path.basename(code_path)
    loader = TextLoader(code_path)
    source_code = loader.load()

    loader = TextLoader('./trace.txt')
    trace = loader.load()

    crashes_explainer = CrashesExplainerPromptTemplate(input_variables=["source_code", "trace"])

    human_input = crashes_explainer.format(source_code=source_code, trace=trace)

    prompt = PromptTemplate(
        input_variables=["chat_history", "human_input"], template=template
    )

    memory = ConversationBufferMemory(memory_key="chat_history")

    llm_chain = LLMChain(
        llm=OpenAI(openai_api_key="", temperature=0.3,
                   max_tokens=2000),
        prompt=prompt,
        memory=memory

    )

    print("Analyzing")

    respond = llm_chain.predict(human_input=human_input)

    print("Crash report: ", respond)

    respond = llm_chain.predict(human_input=fix_prompt)

    print("Fixing")

    print("repaired code: ", respond)

    # fix_code_path = os.getcwd() + "/" + code_name

    fix_code_path = code_path

    with open(fix_code_path, "w") as file:
        file.write(respond)

    print("Code fixed")
