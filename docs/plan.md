# Intro

Trying to sketch out the plan for how data is to be migrated from one 
instance to another with a configurable transformation in between.

# Steps:

## 1. Deal with User / Orgs

When users / orgs are created you can define their name, however a uid that gets
auto-generated is used to establish the relationship between users / orgs and the
packages that they are related to.  The UID's will be different between PROD and
TEST instances.

The update script will start with an update of Users / Orgs.  The update will:
1. Get all user data for SRC (PROD)
1. Get all user data for DEST (TEST)
1. Determination of Deltas:
   * for each user on SRC do the transformations if necessary
   * remove machine generated fields on SRC and DEST
   * compare objects.

1. get a list of all the users in Test / Prod, get all the data.
1. identify Adds / Deletes / Updates
1. Perform the Adds / Deletes / Updates
1. Create a mapping between usernames and id's that allows the update of dependent
   data to identify differences.

## 2. Identify Mapping of fields between prod / test

A mapping file can be created that describes the differences between the two 
BCDC instances.  If no mapping file is found the update process will assume that 
the update is using a 1:1 between the two schemas.

## 3. Identify Package Insert / Update / Delete 

Need to figure out how the Package / Resource update should take place. 
Initially will try to update the resources as sub items of the package.  Treating
the resources as if they are just extra fields in the package. 

* get a package list from prod. (list of package names)
* get package list from test (list of package names)
* Iterate over each of the packages comparing the package modification dates to 
  identify updates
* identify packages in test but not in prod as deletes
* identify packages in prod but not in test as adds.
* From that list identify deletes and adds.

## 4. Perform Package updates

Previous steps identify what needs to be updated, this process will perform the 
actual updates.  Ie the Deletes / Adds / Inserts.

## 5. Other BCDC Updates

Currently have identified:
   * packages
   * resources
   * users
   * organizations

Other possible objects that will need to be updated:
   * groups
   * tags
   * [licenses](https://docs.ckan.org/en/2.8/api/#ckan.logic.action.get.license_list)



