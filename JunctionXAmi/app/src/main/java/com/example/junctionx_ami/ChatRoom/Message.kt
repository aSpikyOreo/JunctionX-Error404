package com.example.junctionx_ami.ChatRoom
//package com.example.scaledrone.chat;

//class Message(val text: String, val memberData: MemberData, val isBelongsToCurrentUser: Boolean)
class Message(var text2: String, var isBelongsToCurrentUser2: Boolean){

//    fun Message(text: String, belongsToCurrentUser: Boolean): ??? {
//        this.text = text
//        this.belongsToCurrentUser = belongsToCurrentUser
//    }

    fun getText(): String {
        return text2
    }

//    fun getMemberData(): MemberData {
//        return memberData
//    }

    fun isBelongsToCurrentUser(): Boolean {
        return isBelongsToCurrentUser2
    }
}
