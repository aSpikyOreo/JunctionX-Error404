package com.example.junctionx_ami
import android.graphics.Color
import android.graphics.Typeface
import android.graphics.drawable.Drawable
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.core.content.ContextCompat
import com.igalata.bubblepicker.BubblePickerListener
import com.igalata.bubblepicker.adapter.BubblePickerAdapter
import com.igalata.bubblepicker.model.BubbleGradient
import com.igalata.bubblepicker.model.PickerItem
import com.igalata.bubblepicker.rendering.BubblePicker
import kotlinx.android.synthetic.main.activity_welcome.*


class Welcome : AppCompatActivity() {

//    val emotionSet = arrayListOf<String>(
//        "Happy", "Depressed", "Anxious", "Angry", "Content",
//        "Excited", "Productive", "Bored", "Tired", "Sad", "Stressed"
//    )
//    val goodEmotes = arrayListOf<String>("Happy", "Excited", "Productive", "Content")
//    val badEmotes = arrayListOf<String>("Depressed", "Anxious", "Angry", "Bored", "Sad", "Stressed")


//    val emoteBubbes = arrayListOf<Drawable>(R.drawable.happy, R.drawable.depressed, R.drawable.anxious,
//                                     R.drawable.angry, R.drawable.content, R.drawable.excited,
//                                     R.drawable.productive, R.drawable.bored, R.drawable.tired,
//                                     R.drawable.sad, R.drawable.stressed)
//
//
//    val bubbleColors = arrayListOf<Int>(
//        Color.parseColor("#E3DFFF"),
//        Color.parseColor("A4DEF9"),
//        Color.parseColor("#EFBCD5"),
//        Color.parseColor("#AED9E0"),
//        Color.parseColor("#C59FC9")
//    )


    private val boldTypeface by lazy { Typeface.createFromAsset(assets, ROBOTO_BOLD) }
    private val mediumTypeface by lazy { Typeface.createFromAsset(assets, ROBOTO_MEDIUM) }
    private val regularTypeface by lazy { Typeface.createFromAsset(assets, ROBOTO_REGULAR) }

    companion object {
        private const val ROBOTO_BOLD = "roboto_bold.ttf"
        private const val ROBOTO_MEDIUM = "roboto_medium.ttf"
        private const val ROBOTO_REGULAR = "roboto_regular.ttf"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_welcome)

        titleTextView.typeface = mediumTypeface
        subtitleTextView.typeface = boldTypeface
        hintTextView.typeface = regularTypeface
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            subtitleTextView.letterSpacing = 0.06f
            hintTextView.letterSpacing = 0.05f
        }

        val emotions = resources.getStringArray(R.array.emotions)
        val colors = resources.obtainTypedArray(R.array.colors)
        val images = resources.obtainTypedArray(R.array.images)

        picker.adapter = object : BubblePickerAdapter {

            override val totalCount = emotions.size

            override fun getItem(position: Int): PickerItem {
                return PickerItem().apply {
                    title = emotions[position]
                    gradient = BubbleGradient(colors.getColor((position * 2) % 8, 0),
                        colors.getColor((position * 2) % 8 + 1, 0), BubbleGradient.VERTICAL)
                    typeface = mediumTypeface
                    textColor = ContextCompat.getColor(this@Welcome, android.R.color.white)
                    backgroundImage = ContextCompat.getDrawable(this@Welcome, images.getResourceId(position, 0))
                }
            }
        }

        colors.recycle()
        images.recycle()

        picker.bubbleSize = 20
        picker.listener = object : BubblePickerListener {
            override fun onBubbleSelected(item: PickerItem) = toast("${item.title} selected")

            override fun onBubbleDeselected(item: PickerItem) = toast("${item.title} deselected")
        }
    }

    override fun onResume() {
        super.onResume()
        picker.onResume()
    }

    override fun onPause() {
        super.onPause()
        picker.onPause()
    }

    private fun toast(text: String) = Toast.makeText(this, text, Toast.LENGTH_SHORT).show()

}


//
//    var bubblePickerListener = object : BubblePickerListener {
//        override fun onBubbleSelected(item: PickerItem) {
//            Toast.makeText(applicationContext, "" + item.title + " selected", Toast.LENGTH_SHORT)
//                .show()
//
//        }
//
//        override fun onBubbleDeselected(item: PickerItem) {
//            Toast.makeText(applicationContext, "" + item.title + " DeSelected", Toast.LENGTH_SHORT)
//                .show()
//
//        }
//    }


//    val bubblePicker : BubblePicker = findViewById(R.id.picker)
//
//    val num_emotions = emotionSet.size
//    var listItems = ArrayList<PickerItem>()
//    for (e in 0 until num_emotions){
//        var item : PickerItem = PickerItem(title = emotionSet[e], color = bubbleColors[e], textColor = Color.WHITE)
//        listItems.add(item)
//    }
//
//    bubblePicker.selectedItems
//}


