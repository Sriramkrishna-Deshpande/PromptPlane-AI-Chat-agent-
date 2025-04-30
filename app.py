import gradio as gr
from langchain_groq import ChatGroq

# Initialize Groq LLM
llm = ChatGroq(
    temperature=1.5,
    model="llama-3.3-70b-versatile",
    groq_api_key=""# Paste your Groq Llama API Key
)

# Define response function
def get_response(input_text):
    res = llm.invoke(input_text)
    return res.content

# Build the Gradio interface
with gr.Blocks(css="""
    #send-btn {
        background-color: #f97316 !important;  /* Orange */
        color: white !important;
        border: none;
        font-weight: bold;
    }
""") as demo:

    # Title
    gr.Markdown("""
        <h1 style="text-align: center; color: #1E3A8A;"> PromptPlane – AI Chat Agent</h1>
        <p style="text-align: center;">Your intelligent Chat Agent powered by Llama.</p>
        <hr>
    """)

    # Output display
    output_box = gr.Textbox(
        label="AI Response",
        lines=20,
        interactive=False,
        show_label=False
    )

    # Input and send on same line, no custom height or padding
    with gr.Row():
        input_box = gr.Textbox(
            placeholder="Type your message...",
            lines=1,
            show_label=False,
            scale=9
        )
        send_button = gr.Button("Send", scale=1, elem_id="send-btn")

    # Bind logic
    send_button.click(fn=get_response, inputs=input_box, outputs=output_box)
    input_box.submit(fn=get_response, inputs=input_box, outputs=output_box)

# Launch app
demo.launch(share=True)
