import os
#运行此文件，更新概述目录
def generate_readme():
    courses_dir = 'courses'
    readme_path = 'README.md'
    
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write('# 南开大学软件工程课程共享\n\n')
        readme_file.write('本项目旨在收集和分享南开大学软件工程专业课程的学习资料和经验\n\n')
        readme_file.write('## 如何贡献\n')
        readme_file.write('欢迎大家贡献自己的学习资料和经验。请参考 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何贡献。\n\n')


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
