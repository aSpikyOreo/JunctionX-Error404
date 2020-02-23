package com.example.scaledrone.chat

//import android.R.*
import android.os.Bundle
//import android.support.v7.app.AppCompatActivity
import android.view.View
import android.widget.EditText
import android.widget.ListView

import androidx.appcompat.app.AppCompatActivity
import com.example.junctionx_ami.ChatRoom.Message
import com.example.junctionx_ami.R

import com.fasterxml.jackson.core.JsonProcessingException
import com.fasterxml.jackson.databind.JsonNode
import com.fasterxml.jackson.databind.ObjectMapper
import com.scaledrone.lib.Listener
import com.scaledrone.lib.Member
import com.scaledrone.lib.Room
import com.scaledrone.lib.RoomListener
import com.scaledrone.lib.Scaledrone

import java.util.Random

//import androidx.test.internal.runner.junit4.statement.UiThreadStatement.runOnUiThread

class MessageAMI : AppCompatActivity(), RoomListener {

    // replace this with a real channelID from Scaledrone dashboard
    private val channelID = "CHANNEL_ID_FROM_YOUR_SCALEDRONE_DASHBOARD"
    private val roomName = "observable-room"
    private var editText: EditText? = null
    private var scaledrone: Scaledrone? = null
    private var messageAdapter: MessageAdapter? = null
    private var messagesView: ListView? = null


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_messageami)

        editText = findViewById(R.id.editText) as EditText

        messageAdapter = MessageAdapter(this)
        messagesView = findViewById(R.id.messages_view) as ListView
        messagesView!!.adapter = messageAdapter

//        val data = MemberData(randomName, randomColor)

        scaledrone = Scaledrone(channelID, null)
        scaledrone!!.connect(object : Listener {
            override fun onOpen() {
                println("Scaledrone connection open")
                scaledrone!!.subscribe(roomName, this@MessageAMI)
            }

            override fun onOpenFailure(ex: Exception) {
                System.err.println(ex)
            }

            override fun onFailure(ex: Exception) {
                System.err.println(ex)
            }

            override fun onClosed(reason: String) {
                System.err.println(reason)
            }
        })
    }

    fun sendMessage(view: View) {
        val message = editText!!.text.toString()
        if (message.length > 0) {
            scaledrone!!.publish(roomName, message)
            editText!!.text.clear()
        }
    }

    override fun onOpen(room: Room) {
        println("Conneted to room")
    }

    override fun onOpenFailure(room: Room, ex: Exception) {
        System.err.println(ex)
    }

    override fun onMessage(room: Room, receivedMessage: com.scaledrone.lib.Message) {
        val mapper = ObjectMapper()
        try {
//            val data = mapper.treeToValue(receivedMessage.member.clientData, MemberData::class.java)
            val belongsToCurrentUser = receivedMessage.clientID == scaledrone!!.clientID
            val message = Message(receivedMessage.data.asText(), belongsToCurrentUser)
            runOnUiThread {
                messageAdapter!!.add(message)
                messagesView!!.setSelection(messagesView!!.count - 1)
            }
        } catch (e: JsonProcessingException) {
            e.printStackTrace()
        }

    }
}
