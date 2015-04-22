from flask import Flask, request, make_response, Response
import plivo, plivoxml

app = Flask(__name__)

@app.route('/forward_sms/', methods=['GET','POST'])
def inbound_sms():

    # Sender's phone number
    from_number = request.values.get('From')

    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')

    # The text which was received
    text = request.values.get('Text')

    # Print the message
    print 'Text received: %s - From: %s' % (text, from_number)

    # Generate a Message XML with the details of the reply to be sent

    resp = plivoxml.Response()

    # The phone number to which the SMS has to be forwarded
    to_forward = '3333333333'

    body = 'Forwarded message : %s' % (text)
    params = {
    'src' : to_number, # Sender's phone number
    'dst' : to_forward, # Receiver's phone number
    }

    # Message added
    resp.addMessage(body, **params)

    # Prints the XML
    print resp.to_xml()
    # Returns the XML
    return Response(str(resp),mimetype='text/xml')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
