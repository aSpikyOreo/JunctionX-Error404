package com.example.junctionx_ami
import android.graphics.Typeface
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.core.content.ContextCompat
import com.igalata.bubblepicker.BubblePickerListener
import com.igalata.bubblepicker.adapter.BubblePickerAdapter
import com.igalata.bubblepicker.model.BubbleGradient
import com.igalata.bubblepicker.model.PickerItem
import kotlinx.android.synthetic.main.activity_welcome.*
import java.lang.Math.random


class Welcome : AppCompatActivity() {

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

        hintTextView.typeface = regularTypeface
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
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
                    gradient = BubbleGradient(colors.getColor((random().toInt() * 2) % 8, 1),
                        colors.getColor((random().toInt() * 2) % 8 + 2, 4), BubbleGradient.HORIZONTAL)
                    typeface = mediumTypeface
                    textColor = ContextCompat.getColor(this@Welcome, android.R.color.white)
                    backgroundImage = ContextCompat.getDrawable(this@Welcome, images.getResourceId(position, 0))
                }
            }
        }

        colors.recycle()
        images.recycle()

        picker.bubbleSize = 45
        picker.listener = object : BubblePickerListener {
            override fun onBubbleSelected(item: PickerItem) = toast("")//"${item.title} selected")

            override fun onBubbleDeselected(item: PickerItem) = toast("")//""${item.title} deselected")
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



