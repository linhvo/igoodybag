from django.db import models

# Create your models here.
class Users(models.Model):
 # id = models.IntegerField(primary_key=True)
  email = models.TextField(unique=True, blank=True)
  password = models.TextField(blank=True)
  singlyaccesstoken = models.TextField(db_column='singlyAccessToken', blank=True) # Field name made lowercase.
  singlyid = models.TextField(unique=True, db_column='singlyId', blank=True) # Field name made lowercase.

  def __unicode__(self):
    return str(self.email)

  class Meta:
    db_table = u'users'

class Charities(models.Model):
  #id = models.IntegerField(primary_key=True)
  name = models.TextField(blank=True)
  desc = models.TextField(blank=True)
  logourl = models.TextField(db_column='logoUrl', blank=True) # Field name made lowercase.
  joineddate = models.DateTimeField(null=True, db_column='joinedDate', blank=True) # Field name made lowercase.
  totalreceived = models.FloatField(null=True, db_column='totalReceived', blank=True) # Field name made lowercase.

  def __unicode__(self):
    return self.name

  class Meta:
    db_table = u'charities'

class Businesses(models.Model):
  #id = models.IntegerField(unique=True)
  charityid = models.ForeignKey(Charities, null=True, db_column='charityId', blank=True) # Field name made lowercase.
  name = models.TextField(blank=True)
  url = models.TextField(blank=True)
  logourl = models.TextField(db_column='logoUrl', blank=True) # Field name made lowercase.
  cardcode = models.TextField(db_column='cardCode', blank=True) # Field name made lowercase.
  menudescription = models.TextField(db_column='menuDescription', blank=True) # Field name made lowercase.
  street1 = models.TextField(blank=True)
  street2 = models.TextField(blank=True)
  city = models.TextField(blank=True)
  state = models.TextField(blank=True)
  zip = models.IntegerField(null=True, blank=True)
  isgb = models.NullBooleanField(null=True, db_column='isGB', blank=True) # Field name made lowercase.
  isverified = models.NullBooleanField(null=True, db_column='isVerified', blank=True) # Field name made lowercase.
  isenabled = models.NullBooleanField(null=True, db_column='isEnabled', blank=True) # Field name made lowercase.
  isdeleted = models.NullBooleanField(null=True, db_column='isDeleted', blank=True) # Field name made lowercase.
  isflagged = models.NullBooleanField(null=True, db_column='isFlagged', blank=True) # Field name made lowercase.
  comment = models.TextField(blank=True)
  createdat = models.DateTimeField(null=True, db_column='createdAt', blank=True) # Field name made lowercase.
  updatedat = models.DateTimeField(null=True, db_column='updatedAt', blank=True) # Field name made lowercase.

  def __unicode__(self):
    return self.name

  class Meta:
    db_table = u'businesses'

class Businessloyaltysettings(models.Model):
  #id = models.IntegerField(primary_key=True)
  businessid = models.ForeignKey(Businesses, unique=True, null=True, db_column='businessId', blank=True) # Field name made lowercase.
  reward = models.TextField(blank=True)
  requireditem = models.TextField(db_column='requiredItem', blank=True) # Field name made lowercase.
  regularpunchesrequired = models.IntegerField(null=True, db_column='regularPunchesRequired', blank=True) # Field name made lowercase.
  elitepunchesrequired = models.IntegerField(null=True, db_column='elitePunchesRequired', blank=True) # Field name made lowercase.
  punchesrequiredtobecomeelite = models.IntegerField(null=True, db_column='punchesRequiredToBecomeElite', blank=True) # Field name made lowercase.
  photourl = models.TextField(db_column='photoUrl', blank=True) # Field name made lowercase.

  class Meta:
    db_table = u'businessLoyaltySettings'

class Businesstags(models.Model):
 # id = models.IntegerField(primary_key=True)
  businessid = models.ForeignKey(Businesses, null=True, db_column='businessId', blank=True) # Field name made lowercase.
  tag = models.TextField(blank=True)
  createdat = models.DateTimeField(null=True, db_column='createdAt', blank=True) # Field name made lowercase.
  class Meta:
    db_table = u'businessTags'

class Locations(models.Model):
  #id = models.IntegerField(unique=True)
  businessid = models.ForeignKey(Businesses, null=True, db_column='businessId', blank=True) # Field name made lowercase.
  name = models.TextField(blank=True)
  street1 = models.TextField(blank=True)
  street2 = models.TextField(blank=True)
  city = models.TextField(blank=True)
  state = models.TextField(blank=True)
  zip = models.IntegerField(null=True, blank=True)
  country = models.TextField(blank=True)
  phone = models.TextField(blank=True)
  fax = models.TextField(blank=True)
  lat = models.FloatField(null=True, blank=True)
  lon = models.FloatField(null=True, blank=True)
  position = models.TextField(blank=True) # This field type is a guess.
  startsunday = models.TimeField(null=True, db_column='startSunday', blank=True) # Field name made lowercase.
  endsunday = models.TimeField(null=True, db_column='endSunday', blank=True) # Field name made lowercase.
  startmonday = models.TimeField(null=True, db_column='startMonday', blank=True) # Field name made lowercase.
  endmonday = models.TimeField(null=True, db_column='endMonday', blank=True) # Field name made lowercase.
  starttuesday = models.TimeField(null=True, db_column='startTuesday', blank=True) # Field name made lowercase.
  endtuesday = models.TimeField(null=True, db_column='endTuesday', blank=True) # Field name made lowercase.
  startwednesday = models.TimeField(null=True, db_column='startWednesday', blank=True) # Field name made lowercase.
  endwednesday = models.TimeField(null=True, db_column='endWednesday', blank=True) # Field name made lowercase.
  startthursday = models.TimeField(null=True, db_column='startThursday', blank=True) # Field name made lowercase.
  endthursday = models.TimeField(null=True, db_column='endThursday', blank=True) # Field name made lowercase.
  startfriday = models.TimeField(null=True, db_column='startFriday', blank=True) # Field name made lowercase.
  endfriday = models.TimeField(null=True, db_column='endFriday', blank=True) # Field name made lowercase.
  startsaturday = models.TimeField(null=True, db_column='startSaturday', blank=True) # Field name made lowercase.
  endsaturday = models.TimeField(null=True, db_column='endSaturday', blank=True) # Field name made lowercase.
  isenabled = models.NullBooleanField(null=True, db_column='isEnabled', blank=True) # Field name made lowercase.
  lastkeytagrequest = models.DateTimeField(null=True, db_column='lastKeyTagRequest', blank=True) # Field name made lowercase.
  keytagrequestpending = models.NullBooleanField(null=True, db_column='keyTagRequestPending', blank=True) # Field name made lowercase.

  def __unicode__(self):
    return self.name

  class Meta:
    db_table = u'locations'

class Cashiers(models.Model):
 # id = models.IntegerField(primary_key=True)
  userid = models.ForeignKey(Users, unique=True, null=True, db_column='userId', blank=True) # Field name made lowercase.
  businessid = models.ForeignKey(Businesses, null=True, db_column='businessId', blank=True) # Field name made lowercase.
  locationid = models.ForeignKey(Locations, null=True, db_column='locationId', blank=True) # Field name made lowercase.
  cardid = models.TextField(db_column='cardId', blank=True) # Field name made lowercase.

  def __unicode__(self):
    return self.cardid

  class Meta:
    db_table = u'cashiers'

class Tapinstations(models.Model):
  #id = models.IntegerField(primary_key=True)
  userid = models.ForeignKey(Users, null=True, db_column='userId', blank=True) # Field name made lowercase.
  businessid = models.ForeignKey(Businesses, null=True, db_column='businessId', blank=True) # Field name made lowercase.
  locationid = models.ForeignKey(Locations, null=True, db_column='locationId', blank=True) # Field name made lowercase.
  loyaltyenabled = models.NullBooleanField(null=True, db_column='loyaltyEnabled', blank=True) # Field name made lowercase.
  galleryenabled = models.NullBooleanField(null=True, db_column='galleryEnabled', blank=True) # Field name made lowercase.
  class Meta:
    db_table = u'tapinStations'

class Tapins(models.Model):
  #id = models.IntegerField(primary_key=True)
  userid = models.ForeignKey(Users, null=True, db_column='userId', blank=True) # Field name made lowercase.
  tapinstationid = models.ForeignKey(Tapinstations, null=True, db_column='tapinStationId', blank=True) # Field name made lowercase.
  cardid = models.TextField(db_column='cardId', blank=True) # Field name made lowercase.
  datetime = models.DateTimeField(db_column='dateTime') # Field name made lowercase.
  class Meta:
    db_table = u'tapins'