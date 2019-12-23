import neptune
neptune.init('shared/onboarding', api_token='eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vdWkubmVwdHVuZS5tbCIsImFwaV9rZXkiOiJiNzA2YmM4Zi03NmY5LTRjMmUtOTM5ZC00YmEwMzZmOTMyZTQifQ==')
with neptune.create_experiment(name='hello-neptune'):
 	neptune.append_tag('introduction-minimal-example')
 	n = 117
 	for i in range(1, n):
 		neptune.log_metric('iteration', i)
 		neptune.log_metric('loss', 1/i**0.5)
 		neptune.log_text('magic values', 'magic value{}'.format(0.95*i**2))
 	neptune.set_property('n_iterations', n)