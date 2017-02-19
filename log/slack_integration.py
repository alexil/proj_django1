import logging
import json


def print_errors_num():
    import os
    import errno
    # print {i: os.strerror(i) for i in sorted(errno.errorcode)}
    for i in sorted(errno.errorcode):
        print i, ': ', os.strerror(i)

def slack_main():
    from slackclient import SlackClient
    CONST_1 = '138124701906'
    _x_oxp = 'xoxp' +'-'+CONST_1
    sc = SlackClient(_x_oxp + '-138056302915-138289150725-c915eb1979c0f442e0e1cc3531d085b0')
    sc = SlackClient(_x_oxp + '-138056302915-139744994305-5e0e855df570dbb3fafe6d954f9b40c7')
    sc = SlackClient(_x_oxp + '-138323863829-139645091936-57b5e45955df53ad13c4bda8ff3907f0')
    # api_call = sc.api_call("im.list")
    # if api_call.get('ok'):
    #     for im in api_call.get("ims"):
    #         print im
    # pass
    u_list = sc.api_call("users.list")
    im_list = sc.api_call("im.list")
    print ' ------------------ '
    print u_list
    for u in u_list['members']:

        channel = u['id']
        u_name = u['name']
        print u_name, channel

        a = sc.api_call(
            "chat.postMessage"
            # , channel='@o526'
            , channel=channel
            # , channel='#ttt-1'
            # , channel="@sco-notificator"
            # , channel=channel
            # , channel="U421N8WSX"  #Oleg
            # , channel="D41GC3Q2V"   #Olegchannel
            # , channel="@scourge"
            # , channel="#general"
            , as_user = True
            , text='-- text ---hhhhh------'
            , type= "error"
            , username='#test'
            , attachments=[
                 {"pretext": channel, "text": u_name, "color":"#000000"}
                ,{"pretext": 'pretext', "text": 'text', 'title':"Title:" + u_name+' ====== ' + channel, "color":"danger"}
                ]
            , icon_url='http://lorempixel.com/48/48'
            # , icon_emoji=':chart_with_upwards_trend:'
        )


    # print a
    u_list = sc.api_call("users.list")
    im_list = sc.api_call("im.list")
    print ' ------------------ '
    print u_list
    for u in u_list['members']:
        print u['name'], u['id']

    # api_call = sc.api_call("im.list")
    # if api_call.get('ok'):
    #     for im in api_call.get("ims"):
    #         print  'user : ', im.get("user")
    #         print im.get("id")
    #
    # rrrr = sc.api_call("rtm.start")
    # print rrrr
    pass


if __name__ == "__main__":
    # print_errors_num()
    slack_main()