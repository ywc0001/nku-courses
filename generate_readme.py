import os

def generate_readme():
    courses_dir = 'courses'
    readme_path = 'README.md'
    
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write('# 南开大学课程共享攻略\n\n')
        readme_file.write('本项目旨在收集和分享南开大学各专业课程的学习资料和经验，帮助南开学子更好地学习和成长。\n\n')
        readme_file.write('## 目录\n\n')
        
        for subject in sorted(os.listdir(courses_dir)):
            subject_dir = os.path.join(courses_dir, subject)
            if os.path.isdir(subject_dir):
                readme_file.write(f'- [{subject}](courses/{subject}/)\n')
                
                for course in sorted(os.listdir(subject_dir)):
                    course_dir = os.path.join(subject_dir, course)
                    if os.path.isdir(course_dir):
                        readme_file.write(f'  - [{course}](courses/{subject}/{course}/)\n')

if __name__ == '__main__':
    generate_readme()
