from enum import Enum

class NotificationType(str, Enum):
    WELCOME = "WELCOME"
    COURSE_PUBLISHED = "COURSE_PUBLISHED"
    COURSE_UPDATED = "COURSE_UPDATED"
    SYSTEM = "SYSTEM"