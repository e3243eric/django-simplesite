from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

# Regular Expression
import re

# Check the password contain lower characters.
class ContainLowerCharacter:
  def __init__(self, min_contain=1):
    self.min_contain = min_contain

  def validate(self, password, user=None):
    count = 0
    for character in password:
      if character.islower():
        count += 1

    if count < self.min_contain:
      raise ValidationError(
        _("This password must contain at least %d lower characters."),
        code='password_need_lower_character',
        params=self.min_contain,
      )

  def get_help_text(self):
    return _(
      "Your password must contain at least %d lower characters."
      % self.min_contain
    )

# Check the password contain upper characters.
class ContainUpperCharacter:
  def __init__(self, min_contain=1):
    self.min_contain = min_contain

  def validate(self, password, user=None):
    count = 0
    for character in password:
      if character.isupper():
        count += 1

    if count < self.min_contain:
      raise ValidationError(
        _("This password must contain at least %d upper characters."),
        code='password_need_upper_character',
        params=self.min_contain,
      )

  def get_help_text(self):
    return _(
      "Your password must contain at least %d upper characters."
      % self.min_contain
    )

# Check the password contain digits characters.
class ContainDigitCharacter:
  def __init__(self, min_contain=1):
    self.min_contain = min_contain

  def validate(self, password, user=None):
    count = 0
    for character in password:
      if character.isdigit():
        count += 1

    if count < self.min_contain:
      raise ValidationError(
        _("This password must contain at least %d digit characters."),
        code='password_need_digit_character',
        params=self.min_contain,
      )

  def get_help_text(self):
    return _(
      "Your password must contain at least %d digit characters."
      % self.min_contain
    )

# Check the password contain special characters.
class ContainSpecialCharacter:
  def __init__(self):
    self.regular_expression = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

  def validate(self, password, user=None):
    if self.regular_expression.search(password) == None:
      raise ValidationError(
        _("This password must contain at least 1 special characters.(%s)"),
        code='password_need_special_character',
        params=self.regular_expression.pattern,
      )

  def get_help_text(self):
    return _(
      "Your password must contain at least 1 special characters.(%s)"
      % self.regular_expression.pattern
    )