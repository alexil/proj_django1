import logging
import json


def slack_main():
    from     slackclient    import SlackClient
    # sc = SlackClient('xoxp-138124701906-138056302915-138289150725-c915eb1979c0f442e0e1cc3531d085b0')
    sc = SlackClient('xoxb-139551511888-vlltqKYjUJGMIvU0rYwLKWLk')

    sc.api_call(
        "chat.postMessage"
        , channel="#ttt-1"
        # , channel="#general"
        , text='----00-3----Hello from Python! \n:tada:  \n :chart_with_upwards_trend:'
        , type= "error"
        , username='/SCO/'
        # , attachments=[{"pretext": "pre-hello", "text": "text-world", "color":"#36a64f"},{'title':'== TiTle ====', "color":"danger"}]
        , icon_url='http://lorempixel.com/48/48'
        # , icon_emoji=':chart_with_upwards_trend:'
        , attachments=[
            {
            "fallback": "---- fallback ticket from Andrea Lee - Ticket #1943: Can't rest my password - https://groove.hq/path/to/ticket/1943",
            "pretext": "====== >> New pretext <<  ====== ",
            "title": "Ticket #1943: Can't reset my password",
            "title_link": "https://groove.hq/path/to/ticket/1943",
            "text": "Help! I tried to reset my password but nothing happened!",
            "color": "#7CD197"
            }
        ]


    )
    pass


if __name__ == "__main__":
    # main()
    slack_main()