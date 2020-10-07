# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by zhiweiyang
# Create At: 2020/7/31

import xml.etree.ElementTree as ET
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.utils import check_signature
from flask import Flask, request, jsonify
from github_tool import GithubIssue
from secrets import *
from WXBizMsgCrypt import WXBizMsgCrypt
import time


app = Flask(__name__)


class Msg(object):
    def __init__(self, xmldata):
        self.ToUserName = xmldata.find('ToUserName').text
        self.FromUserName = xmldata.find('FromUserName').text
        self.CreateTime = xmldata.find('CreateTime').text
        self.MsgType = xmldata.find('MsgType').text
        self.MsgId = xmldata.find('MsgId').text


class TextMsg(Msg):
    def __init__(self, tousername, fromusername, content, xmldata):
        super(TextMsg, self).__init__(xmldata)
        self.__dict = dict()
        self.__dict['ToUserName'] = tousername
        self.__dict['FromUserName'] = fromusername
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self, nonce):
        xmlform = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        encryp_test = WXBizMsgCrypt(token, encoding_aes_key, appid)
        ret, encrypt_xml = encryp_test.EncryptMsg(xmlform.format(**self.__dict), nonce)
        return encrypt_xml


def autoreply(decryp_xml, nonce):
    decryp_xml = ET.fromstring(decryp_xml)
    msg_type = decryp_xml.find('MsgType').text
    tousername = decryp_xml.find('ToUserName').text
    fromusername = decryp_xml.find('FromUserName').text
    in_msg = decryp_xml.find('Content').text
    touser, fromuser = fromusername, tousername
    github = GithubIssue()
    if msg_type == 'text':
        im_msgs = in_msg.split(" ")
        github.create_an_issues(im_msgs[0], in_msg)
        issue_numbers = github.get_issue_list()
        msg = github.get_issue_detail(issue_numbers[0])
        replymsg = TextMsg(touser, fromuser, msg, decryp_xml)
        return replymsg.send(nonce)

    elif msg_type == 'image':
        content = "图片已收到,谢谢"
        replymsg = TextMsg(touser, fromuser, content, decryp_xml)
        return replymsg.send(nonce)
    elif msg_type == 'voice':
        content = "语音已收到,谢谢"
        replymsg = TextMsg(touser, fromuser, content, decryp_xml)
        return replymsg.send(nonce)
    elif msg_type == 'video':
        content = "视频已收到,谢谢"
        replymsg = TextMsg(touser, fromuser, content, decryp_xml)
        return replymsg.send(nonce)
    elif msg_type == 'shortvideo':
        content = "小视频已收到,谢谢"
        replymsg = TextMsg(touser, fromuser, content, decryp_xml)
        return replymsg.send(nonce)
    elif msg_type == 'location':
        content = "位置已收到,谢谢"
        replymsg = TextMsg(touser, fromuser, content, decryp_xml)
        return replymsg.send(nonce)
    else:
        content = "链接已收到,谢谢"
        replymsg = TextMsg(touser, fromuser, content, decryp_xml)
        return replymsg.send(nonce)


@app.route('/api/token_check/', methods=["POST"])
def wechat():
    data = request.args
    signature = data.get("signature", "")
    timestamp = data.get("timestamp", "")
    nonce = data.get("nonce", "")
    echo_str = data.get("echostr", "")
    msg_signature = data.get("msg_signature", "")

    try:
        check_signature(token, signature, timestamp, nonce)
    except InvalidSignatureException:
        print('InvalidSignatureException')
    if request.method == "GET":
        return jsonify(echo_str)
    else:
        decrypt_test = WXBizMsgCrypt(token, encoding_aes_key, appid)
        ret, decryp_xml = decrypt_test.DecryptMsg(request.data, msg_signature, timestamp, nonce)
        print("decryp_xml: %s" % decryp_xml)
        othercontent = autoreply(decryp_xml, nonce)
        return jsonify(othercontent)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)