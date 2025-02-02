from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from output_parsers import summary_parser, ice_breaker_parser, topics_of_interest_parser

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
llm_creative = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")
# gpt4 llm
llm4 = ChatOpenAI(temperature=0, model_name="gpt-4")


def get_summary_chain() -> LLMChain:
    summary_template = """
         given the information about a person from the web {information} I want you to create:
         1. a short summary
         2. two interesting facts about them
         \n{format_instructions}
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    return LLMChain(llm=llm4, prompt=summary_prompt_template, verbose=True)


def get_interests_chain() -> LLMChain:
    interesting_facts_template = """
         given the information about a person from the web {information} I want you to create:
         3 topics that might interest them
        \n{format_instructions}
     """

    interesting_facts_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=interesting_facts_template,
        partial_variables={
            "format_instructions": topics_of_interest_parser.get_format_instructions()
        },
    )

    return LLMChain(llm=llm4, prompt=interesting_facts_prompt_template)


def get_ice_breaker_chain() -> LLMChain:
    ice_breaker_template = """
         given the information about a person from the web {information} I want you to create:
         2 creative Ice breakers with them that are derived from their activities
        \n{format_instructions}
     """

    ice_breaker_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=ice_breaker_template,
        partial_variables={
            "format_instructions": ice_breaker_parser.get_format_instructions()
        },
    )

    return LLMChain(llm=llm4, prompt=ice_breaker_prompt_template)
