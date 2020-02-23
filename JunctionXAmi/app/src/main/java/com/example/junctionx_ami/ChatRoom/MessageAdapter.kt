package com.example.scaledrone.chat

//import android.R
import com.example.junctionx_ami.R

import android.app.Activity
import android.content.Context
import android.graphics.Color
import android.graphics.drawable.GradientDrawable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.TextView
import com.example.junctionx_ami.ChatRoom.Message

import java.util.ArrayList


class MessageAdapter(internal var context: Context) : BaseAdapter() {

    internal var messages: MutableList<Message> = ArrayList<Message>()


    fun add(message: Message) {
        this.messages.add(message)
        notifyDataSetChanged()
    }

    override fun getCount(): Int {
        return messages.size
    }

    override fun getItem(i: Int): Any {
        return messages[i]
    }

    override fun getItemId(i: Int): Long {
        return i.toLong()
    }

    override fun getView(i: Int, convertView: View, viewGroup: ViewGroup): View {
        var convertView = convertView
        val holder = MessageViewHolder()
        val messageInflater =
            context.getSystemService(Activity.LAYOUT_INFLATER_SERVICE) as LayoutInflater
        val message = messages[i]

        if (message.isBelongsToCurrentUser()) {
            convertView = messageInflater.inflate(R.layout.messageami_usermessage, null)
            holder.messageBody = convertView.findViewById(R.id.message_body) as TextView
            convertView.tag = holder
            holder.messageBody!!.setText(message.getText())
        } else {
            convertView = messageInflater.inflate(R.layout.messageami_amimessage, null)
            holder.avatar = convertView.findViewById(R.id.avatar) as View
            holder.name = convertView.findViewById(R.id.name) as TextView
            holder.messageBody = convertView.findViewById(R.id.message_body) as TextView
            convertView.tag = holder

            holder.name!!.setText(message.getMemberData().getName())
            holder.messageBody!!.setText(message.getText())
            val drawable = holder.avatar!!.background as GradientDrawable
            drawable.setColor(Color.parseColor(message.getMemberData().getColor()))
        }

        return convertView
    }

}

internal class MessageViewHolder {
    var avatar: View? = null
    var name: TextView? = null
    var messageBody: TextView? = null
}