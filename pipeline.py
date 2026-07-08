from agents import build_search_agent,bulid_reader_agent ,writer_chain,critic_chain

def run_research_pipeline(topic:str) -> dict:

    state={}
    
    #search Agent Working
    print("\n"+" ="*40)
    print("Search agent is working..")
    print("="*40)

    search_agent= build_search_agent()
    search_result= search_agent.invoke({
        "messages":[("user",f"find recent,reliable and detailed information about: {topic}")]
    })
    state["search_results"] = search_result['messages'][-1].content

    print("\n search result", state['search_results'])

    #Reader Agent
    print("\n"+" ="*40)
    print("Reader agent is scraping top resource")
    print("="*40)

    reader_agent = bulid_reader_agent()
    reader_result = reader_agent.invoke({
        "messages":[("user",
             f"Based on the following search result about '{topic}',"
             f"pick the most relevent URL and scrape it for deeper content.\n\n"
             f"Search Result:\n{state['search_results'][:800]}"
             )]
    })

    state['scrape_content'] = reader_result['messages'][-1].content

    print(state['scrape_content'])

    #step3 _ Write chain
    print("\n"+" ="*40)
    print("Writer is drafting the report")
    print("="*40)

    research_combined =(
        f"Search Result:\n {state['search_results']}\n\n"
        f"Detailed Scrape Content: \n{state['scrape_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic":topic,
        "research":research_combined
    })

    print("\n Final Report \n ",state["report"])

    #Critic Report
    print("\n"+" ="*40)
    print("Critic is reviewing the report")
    print("="*40)

    state["feedback"] = critic_chain.invoke({
        "report" :state['report']
    })

    print("\n critic report \n",state['feedback'])

    return state

if __name__=="__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)


   


