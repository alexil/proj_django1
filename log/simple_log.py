import logging
import json


# logging.warning("Warning, Will Robinson!")
# logging.debug("This is a debug message!")



def main():
    aaa={'q1':[{'source_version': 'version_1', 'source': 'aggrigator_1', 'confidence': '1', 'name': 'n1'},
    {'source_version': 'version_3', 'source': 'aggrigator_3', 'confidence': '3', 'name': 'n3'}]
         }
    print aaa
    aaa=[{"source_version":"version_1","source":"aggrigator_1","confidence":"1","name":"n1"},{"source_version":"version_3","source":"aggrigator_3","confidence":"3","name":"n3"}]
    print aaa
    ind = list()
    d = {
        "confidence": "1",
        "name": "n1",
        'source': 'aggrigator_1',
        "source_version": "version_1"
    }
    ind.append(d)

    d = {
        "confidence": "2",
        "name": "n2",
        'source': 'aggrigator_2',
        "source_version": "version_2"
    }
    ind.append(d)

    d = {
        str("confidence"): 3,
        "name": "n3",
        'source': 'aggrigator_3',
        "source_version": "version_3"
    }
    ind.append(d)

    rrr = ['{"source_version": "version_1", "source": "aggrigator_1", "confidence": "1", "name": "n1"}',
           '{"source_version": "version_2", "source": "aggrigator_2", "confidence": "2", "name": "n2"}',
           '{"source_version": "version_3", "source": "aggrigator_3", "confidence": 3, "name": "n3"}']

    print "===>>>rrr:", rrr

    print "===", ind
    a = d
    lll = []
    lll.append(d)
    lll.append(d)
    print "lll=>", lll

    print  "a=d  ", d
    # print a["name"]
    sum_list = []
    sss = set()
    for i in ind:
        print i

        sss.add(type(i))
        print a
        if a['name'] not in ["n2"]:
            # sum_list.append(json.dumps(a))
            sum_list.append(a)

    print "summm:",  sum_list
    print '''------------'''
    print sss
    kk = [
          {
            "source_version": "version_1",
            "source": "aggrigator_1",
            "confidence": "1",
            "name": "n1"
          },
          {
            "source_version": "version_3",
            "source": "aggrigator_3",
            "confidence": "3",
            "name": "n3"
          }
        ]
    print kk

    for k in kk:
        print type(k), " ", k
    di1 = dict(w1=1,w2=2,w3=3)
    print di1

    ll1 = ['foo', {'bar': ('baz', None, 1.0, 2)}]
    ddd2 = json.dumps(ll1)
    print type(ll1), ' ', json.dumps(ll1)," ",type(ddd2)

    s1 = '["foo", {"bar":["baz", null, 1.0, 2]}]'
    ddd2 = json.loads(s1)
    print type(s1), ' ', ddd2, type(ddd2)

'''
'''
def slack_main():
    from     slackclient    import SlackClient
    sc = SlackClient('xoxp-138124701906-138056302915-138289150725-c915eb1979c0f442e0e1cc3531d085b0')

    sc.api_call(
        "chat.postMessage"
        , channel="#ttt-1"
        , text='----00-3----Hello from Python! \n:tada:  \n :chart_with_upwards_trend:'
        , type= "error"
        , username='/SCO/'
        # , attachments=[{"pretext": "pre-hello", "text": "text-world", "color":"#36a64f"},{'title':'== TiTle ====', "color":"danger"}]
        , icon_url='http://lorempixel.com/48/48'
        # , icon_emoji=':chart_with_upwards_trend:'
        , attachments=[
            {
            "fallback": "New ticket from Andrea Lee - Ticket #1943: Can't rest my password - https://groove.hq/path/to/ticket/1943",
            "pretext": "New ticket from Andrea Lee",
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