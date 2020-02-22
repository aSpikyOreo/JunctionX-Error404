package com.example.junctionx_ami
import android.graphics.Color
import android.graphics.drawable.Drawable
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.igalata.bubblepicker.BubblePickerListener
import com.igalata.bubblepicker.adapter.BubblePickerAdapter
import com.igalata.bubblepicker.model.PickerItem
import com.igalata.bubblepicker.rendering.BubblePicker
import kotlinx.android.synthetic.main.activity_welcome.*


class Welcome : AppCompatActivity() {

    val emotionSet = arrayListOf<String>("Happy", "Depressed", "Anxious", "Angry", "Content",
                                     "Excited", "Productive", "Bored", "Tired", "Sad", "Stressed")
    val goodEmotes = arrayListOf<String>("Happy","Excited", "Productive", "Content")
    val badEmotes = arrayListOf<String>("Depressed", "Anxious", "Angry", "Bored", "Sad", "Stressed")


//    val emoteBubbes = arrayListOf<Drawable>(R.drawable.happy, R.drawable.depressed, R.drawable.anxious,
//                                     R.drawable.angry, R.drawable.content, R.drawable.excited,
//                                     R.drawable.productive, R.drawable.bored, R.drawable.tired,
//                                     R.drawable.sad, R.drawable.stressed)


    val bubbleColors = arrayListOf<Int>(Color.parseColor("#E3DFFF"),
                                      Color.parseColor("A4DEF9"),
                                      Color.parseColor("#EFBCD5"),
                                      Color.parseColor("#AED9E0"),
                                      Color.parseColor("#C59FC9"))



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_welcome)



        val bubblePicker : BubblePicker = findViewById(R.id.picker)

        val num_emotions = emotionSet.size
        var listItems = ArrayList<PickerItem>()
        for (e in 0 until num_emotions){
            var item : PickerItem = PickerItem(title = emotionSet[e], color = bubbleColors[e], textColor = Color.WHITE)
            listItems.add(item)
        }

        picker.selectedItems
    }
    var bubblePickerListener = object : BubblePickerListener{
        override fun onBubbleSelected(item: PickerItem) {

        }
        override fun onBubbleDeselected(item: PickerItem) {

        }
    }





//    fun collateEmotions(emotions: HashSet<String>){
//        val num_emotions = emotionSet.size
//        var listItems = ArrayList<PickerItem>()
//        for (e in 0 until num_emotions){
//            var item : PickerItem = PickerItem(title = emotionSet[e], color = bubbleColors[e], textColor = Color.WHITE)
//            listItems.add(item)
//        }
//
//        bubblePicker.setItems(listItems)
//    }



}
