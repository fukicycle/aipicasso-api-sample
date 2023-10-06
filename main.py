# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from gradio_client import Client


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    client = Client("https://aipicasso-emi-latest-demo.hf.space/")
    client.output_dir = "C:\\Users\\Gold\\Pictures"
    errorCount = 0
    for i in range(1, 10):
        try:
            result = client.predict(
                "1girl++, cool+, smile--, colorful long hair, colorful eyes, night, pastel color, transparent+",
                # str in 'Prompt' Textbox component
                7.5,  # int | float (numeric value between 0 and 25) in 'Guidance scale' Slider component
                20,  # int | float (numeric value between 2 and 30) in 'Steps' Slider component
                0,  # int | float (numeric value between 0 and 2147483647) in 'Seed (0 = random)' Slider component
                "",  # str in 'Negative prompt' Textbox component
                False,  # bool in 'Disable auto prompt corretion.' Checkbox component
                fn_index=0
            )
            print(result)
        except Exception as e:
            print(e)
            errorCount += 1
        print(f'Finished task. Error count:{errorCount}')
