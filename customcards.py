from PIL import Image, ImageDraw, ImageFont
import csv
import textwrap

fnt = ImageFont.truetype('fonts/times-new-roman.ttf', 30)

# Create image files for all answer cards
with open('input/answers.csv') as ans:
    csv_read = csv.reader(ans, delimiter=',')
    line_count = 0

    for row in csv_read:
        # create a blank card, needed for tts
        if line_count == 0:
            line_count += 1
            img = Image.new('RGB', (300,514), color='white')
            txt = ImageDraw.Draw(img)
            txt.text((20,20), "Cards with the men", font=fnt, fill='black')
            name = 'blank_answer.jpg'
            answer_blank = "output/answers/" + name
            img.save(answer_blank)
        # create an image file for each row
        else:
            img = Image.new('RGB', (300,514), color='white')
            wrap = textwrap.wrap(row[0], width=17)
            height = 20
            for w in wrap:
                txt = ImageDraw.Draw(img)
                txt.text((20,height), w, font=fnt, fill='black')
                height += 30
            
            name = f'image_{line_count}.jpg'
            answer_output = "output/answers/" + name
            img.save(answer_output)
            line_count += 1

    # Create image files for all question cards
    with open('input/questions.csv') as qs:
        csv_read = csv.reader(qs, delimiter=',')
        line_count = 0
        for row in csv_read:
            # Skip first row containing header
            if line_count == 0:
                line_count += 1
                img = Image.new('RGB', (300,514), color='black')
                txt = ImageDraw.Draw(img)
                txt.text((20,20), "Cards with the men", font=fnt, fill='white')
                name = 'blank_question.jpg'
                question_blank = "output/questions/" + name
                img.save(question_blank)
            # create an image file for each row
            else:
                img = Image.new('RGB', (300,514), color='black')
                wrap = textwrap.wrap(row[0], width=17)
                height = 20
                for w in wrap:
                    txt = ImageDraw.Draw(img)
                    txt.text((20,height), w, font=fnt, fill='white')
                    height += 30
                
                name = f'image_{line_count}.jpg'
                questions_output = "output/questions/" + name
                img.save(questions_output)
                line_count += 1




