import os

DEVELOPER_LINKEDIN = "https://www.linkedin.com/in/amatya-katyayan/"

LINKS = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "cc_linkedin": "https://www.linkedin.com/company/cloud-counselage/mycompany/",
    "cc_home": "https://www.cloudcounselage.com/",
    "cc_contact": "https://www.cloudcounselage.com/contactus/",
    "cc_email": "mailto:hrsupport@cloudcounselage.com",
    "drl": "https://cloudcounselage.co.in/#/login",
}

# Internship training tasks on Bitrix24
WEEKS = {
    "week 1": ("Week 1 - Basic Training", "https://cloudcounselage24.bitrix24.com/workgroups/group/180/tasks/task/view/45076/"),
    "week 2": ("Week 2 - Advance Training", "https://cloudcounselage24.bitrix24.com/workgroups/group/180/tasks/task/view/45188/"),
    "week 3": ("Week 3 - Proof of Concept [PoC]", "https://cloudcounselage24.bitrix24.com/workgroups/group/180/tasks/task/view/45308/"),
    "week 4": ("Week 4 - Submission", "https://cloudcounselage24.bitrix24.com/workgroups/group/180/tasks/task/view/45436/"),
}

MUSIC_DIR = os.environ.get("AGRO_MUSIC_DIR", os.path.join(os.path.expanduser("~"), "Music"))
VSCODE = os.environ.get("AGRO_VSCODE", "code")
SPEECH_LANGUAGE = os.environ.get("AGRO_LANGUAGE", "en-in")
